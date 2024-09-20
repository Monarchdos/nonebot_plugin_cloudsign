'''
Name: CloudSign
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2023-01-10 17:22:49
LastEditTime: 2024-09-20 10:30:44
'''
from nonebot import on_regex, logger, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.plugin import PluginMetadata
from .config import Config
import requests
import json
import time
import re

__plugin_meta__ = PluginMetadata(
    name = "☁云签到☁",
    description = "基于云端的签到综合积分系统。",
    usage = "发送'功能'查看。",
    type = "application",
    homepage = "https://github.com/Monarchdos/nonebot_plugin_cloudsign",
    supported_adapters = {"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)

core = '68747470733a2f2f636c6f75647369676e2e61796672652e636f6d2f'
def get_at(data: str) -> list:
    qq_list = []
    data = json.loads(data)
    try:
        for msg in data['message']:
            if msg['type'] == 'at':
                qq_list.append(int(msg['data']['qq']))
    except (KeyError, TypeError, json.JSONDecodeError):
        pass
    return qq_list

qd = on_regex(
    r"^签到$|^积分$|^(挖矿|我的背包|钓鱼|我的鱼篓)$|^(出售|售出) ([\u4e00-\u9fa5]+)$|^功能(?: (.*?))?$|^领取积分补助$|^签到状态$|^排行榜$|^打劫(.*?)$|^抽奖 (\d+)$|^转账 (\d+)(.*?)$|^@检查更新@$|^#(.*?)$|^猜拳(石头|剪刀|布) (\d+)$|^(猜数字|我猜) (\d+)$"
)

@qd.handle()
async def qd_(bot: Bot, event: GroupMessageEvent):
    s = str(event.get_message()).strip()
    username = str(event.sender.nickname)
    ats = get_at(event.json())
    ats = ats[0] if ats else event.user_id
    s = re.sub(r'\[CQ:at,qq=\d+,name=@.*?\]', '', s)
    if not re.match(r'^\d+$', str(event.group_id)): return
    if len(s) > 33 or not s.replace('#', '').replace(' ', ''): return

    version = "2.1.2"

    data = {
        "command": s,
        "at": ats,
        "qq": event.user_id,
        "qun": event.group_id,
        "botqq": event.self_id,
        "username": username,
        "version": version,
        "platform": "qq",
        "token": int(time.time()),
        "key": plugin_config.cloudsign_key if plugin_config.cloudsign_key else "",
        "master": plugin_config.cloudsign_master if plugin_config.cloudsign_master else "",
    }

    try:
        # Simulated requests may ban the IP
        res = requests.post(bytes.fromhex(core).decode(), data).text
        if "wwwroot" in res or "html" in res or len(res) <= 1: return
        reply = ""
        if plugin_config.cloudsign_reply_quote:
            reply = MessageSegment.reply(event.message_id)
        elif plugin_config.cloudsign_reply_at:
            reply = MessageSegment.at(event.user_id) + "\n"
        if res.startswith("[CQ:image,") and "file=" in res:
            file_url = res.split("file=")[-1].strip("]")
            res = MessageSegment.image(file_url)
        await qd.finish(reply + res)
    except requests.RequestException as e:
        logger.warning("Server connection failed.")
