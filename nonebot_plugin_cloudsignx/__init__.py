'''
Name: CloudSign
Author: Monarchdos
Date: 2023-01-10 17:22:49
LastEditTime: 2024-07-14 19:37:06
'''
from nonebot import on_command, on_regex, logger, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, GroupMessageEvent
from nonebot.plugin import PluginMetadata
from .config import Config
import requests
import json
import time

__plugin_meta__ = PluginMetadata(
    name = "☁云签到☁",
    description = "基于云端的签到综合积分系统。",
    usage = "发送'功能'查看。",
    type="application",
    homepage="https://github.com/Monarchdos/nonebot_plugin_cloudsign",
    supported_adapters={"~onebot.v11"},
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
    r"^签到$|^积分$|^(挖矿|我的背包)$|^(钓鱼|我的鱼篓)$|^功能$|^功能 (.*?)$|^领取积分补助$|^签到状态$|^排行榜$|^打劫(.*?)$|^抽奖 (\d+)$|^(出售|售出) ([\u4e00-\u9fa5]+)$|^转账 (\d+)(.*?)$|^(@检查更新@)$|^#(.*?)$|^(猜拳石头|猜拳剪刀|猜拳布) (\d+)$|^(猜数字|我猜) (\d+)$"
)

@qd.handle()
async def qd_(bot: Bot, event: GroupMessageEvent):
    s = str(event.get_message()).strip()
    username = str(event.sender.nickname)
    ats = get_at(event.json())
    ats = ats[0] if ats else event.user_id
    s = s.replace(f"[CQ:at,qq={ats}]", "")
    if len(s) > 66: return

    version = "2.1.0"

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
    if event.user_id != 80000000:
        try:
            # Simulated requests may ban the IP
            response = requests.post(bytes.fromhex(core).decode(), data)
            res = ("\n" if plugin_config.cloudsign_reply_at else "") + response.text
            if "wwwroot" in res or "html" in res or len(res) == 1: return
            await qd.send(message=Message(res), at_sender=plugin_config.cloudsign_reply_at)
        except requests.RequestException as e:
            logger.warning("Server connection failed.")
