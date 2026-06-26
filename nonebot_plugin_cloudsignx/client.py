"""
Name: CloudSign.Client
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2026-06-24
LastEditTime: 2026-06-26
"""
import hmac
import hashlib
import time

import httpx

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


class CloudSignClient:

    def __init__(self, app_key: str, app_secret: str, base_url: str = None):
        self.app_key = app_key
        self.app_secret = app_secret
        self.base_url = (base_url or CORE_URL).rstrip('/')

    async def plugin_request(self, plugin_name: str, qq: int, qun: int,
                             botqq: int, **extra) -> str:
       
        timestamp = int(time.time())
        payload = {
            "qq": qq,
            "qun": qun,
            "botqq": botqq,
            "platform": "nonebot",
            "timestamp": timestamp,
            "app_key": self.app_key,
        }
        payload.update(extra)

        if self.app_secret:
            payload["sign"] = generate_signature(payload, self.app_secret)

        url = f"{self.base_url}?plugin={plugin_name}"

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, data=payload)
            response.raise_for_status()
            return response.text.strip()

    async def command_request(self, command: str, qq: int, qun: int,
                              botqq: int, at: int = 0, **extra) -> str:

        timestamp = int(time.time())
        payload = {
            "command": command,
            "at": at,
            "qq": qq,
            "qun": qun,
            "botqq": botqq,
            "platform": "nonebot",
            "timestamp": timestamp,
            "app_key": self.app_key,
        }
        payload.update(extra)

        if self.app_secret:
            payload["sign"] = generate_signature(payload, self.app_secret)

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(self.base_url, data=payload)
            response.raise_for_status()
            return response.text.strip()
