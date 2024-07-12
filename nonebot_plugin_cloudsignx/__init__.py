'''
Name: CloudSign
Author: Monarchdos
Date: 2023-01-10 17:22:49
LastEditTime: 2024-07-12 15:48:15
'''
from nonebot import on_command
from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment, GroupMessageEvent
from nonebot.plugin import PluginMetadata
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import random
import json
import time
__plugin_meta__ = PluginMetadata(
    name = "☁云签到☁",
    description = "基于云端的签到综合积分系统",
    usage = "发送'功能'查看",
)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = '68747470733a2f2f636c6f75647369676e2e61796672652e636f6d2f'
def get_at(data: str) -> list:
    qq_list = []
    data = json.loads(data)
    try:
        for msg in data['message']:
            if msg['type'] == 'at':
                qq_list.append(int(msg['data']['qq']))
        return qq_list
    except Exception:
        return []

qd = on_regex("^签到$|^积分$|^(挖矿|我的背包)$|^(钓鱼|我的鱼篓)$|^功能$|^功能 (.*?)$|^领取积分补助$|^签到状态$|^排行榜$|^打劫(.*?)$|^抽奖 (\d+)$|^(出售|售出) ([\u4e00-\u9fa5]+)$|^转账 (\d+)(.*?)$|^(@检查更新@)$|^#(.*?)$|^(猜拳石头|猜拳剪刀|猜拳布) (\d+)$|^(猜数字|我猜) (\d+)$")
@qd.handle()
async def qd_(bot: Bot, event: GroupMessageEvent):
    s = str(event.get_message()).strip()
    username = str(event.sender.nickname)
    try:
        ats = get_at(event.json())[0]
    except Exception:
        ats = event.user_id

    s = s.replace("[CQ:at,qq=" + str(ats) + "]", "")
    if len(s) > 66: return

    version = "2.0.0"

    data = {
        "command": s,
        "at": ats,
        "qq": event.user_id,
        "qun": event.group_id,
        "botqq": event.self_id,
        "username": username,
        "version": version,
        "platform": "qq",
        "token": int(time.time())
    }
    
    if event.user_id != "80000000": 
        res = "\n" + str(requests.post(url=bytes.fromhex(url).decode(), data=data, verify=False).text)
        if "wwwroot" in res: return
        if "html" in res: return
        if len(res) == 1: return
        await qd.send(message=Message(res), at_sender=True)