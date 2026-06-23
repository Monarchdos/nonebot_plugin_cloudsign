'''
Name: CloudSign
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2023-01-10 17:22:49
LastEditTime: 2026-06-23 21:30:27
'''
import hmac
import hashlib
import time
import re

import httpx
from nonebot import on_regex, logger, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, Message
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="☁云签到☁",
    description="基于云端的签到综合积分系统。",
    usage="发送'功能'查看。",
    type="application",
    homepage="https://github.com/Monarchdos/nonebot_plugin_cloudsign",
    supported_adapters={"~onebot.v11"},
)

version = "3.0.0"

plugin_config = get_plugin_config(Config)

CORE_URL_HEX = '68747470733a2f2f636c6f75647369676e2e61796672652e636f6d2f'
CORE_URL = bytes.fromhex(CORE_URL_HEX).decode()

def generate_signature(params: dict, app_secret: str) -> str:
    if not app_secret:
        return ""
    sorted_items = sorted(
        (k, str(v)) for k, v in params.items() 
        if v is not None and str(v) != ""
    )
    query_string = "&".join(f"{k}={v}" for k, v in sorted_items)
    return hmac.new(
        app_secret.encode("utf-8"),
        query_string.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

qd = on_regex(
    r"^签到$|^积分$|^(挖矿|我的背包|钓鱼|我的鱼篓)$|^(出售|售出) ([\u4e00-\u9fa5]+)$|^功能(?: (.*?))?$|"
    r"^领取积分补助$|^签到状态$|^排行榜$|^打劫(.*?)$|^抽奖 (\d+)$|^转账 (\d+)(.*?)$|^@检查更新@$|^#(.*?)$|"
    r"^猜拳(石头|剪刀|布) (\d+)$|^(猜数字|我猜) (\d+)$"
)

@qd.handle()
async def handle_cloudsign(bot: Bot, event: GroupMessageEvent):
    command = event.get_plaintext().strip()
    at_segments = event.get_message()["at"]
    target_qq = int(at_segments[0].data["qq"]) if at_segments else event.user_id

    if len(command) > 33 or not command.replace('#', '').strip():
        return

    timestamp = int(time.time())

    payload = {
        "command": command,
        "at": target_qq,
        "qq": event.user_id,
        "qun": event.group_id,
        "botqq": event.self_id,
        "username": event.sender.nickname or "",
        "version": version,
        "platform": "nonebot",
        "timestamp": timestamp,
        "app_key": plugin_config.cloudsign_app_key,
        "master": plugin_config.cloudsign_master,
    }

    if plugin_config.cloudsign_app_secret:
        payload["sign"] = generate_signature(payload, plugin_config.cloudsign_app_secret)

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(CORE_URL, data=payload)
            response.raise_for_status()
            res_text = response.text.strip()

        if not res_text or any(x in res_text for x in ["wwwroot", "html", "<body"]):
            return

        if res_text.startswith("[PRIVATE:"):
            match = re.match(r"\[PRIVATE:(\d+)\](.*)", res_text, re.DOTALL)
            if match:
                target_qq = int(match.group(1))
                content = match.group(2).strip()
                try:
                    await bot.send_private_msg(user_id=target_qq, message=content)
                except Exception:
                    logger.warning(f"私聊发送失败: {target_qq}")
            await qd.finish()

        message = Message()
        if plugin_config.cloudsign_reply_quote:
            message.append(MessageSegment.reply(event.message_id))
        elif plugin_config.cloudsign_reply_at:
            message.append(MessageSegment.at(event.user_id))
            message.append("\n")

        if "[CQ:image," in res_text and "file=" in res_text:
            match = re.search(r"file=(.*?)[,\]]", res_text)
            if match:
                message.append(MessageSegment.image(match.group(1)))
            else:
                message.append(res_text)
        else:
            message.append(res_text)

        await qd.finish(message)

    except httpx.HTTPStatusError as e:
        logger.error(f"Server Error: {e.response.status_code}")
    except httpx.RequestError as e:
        logger.warning(f"无法连接到云签到服务器: {e}")
