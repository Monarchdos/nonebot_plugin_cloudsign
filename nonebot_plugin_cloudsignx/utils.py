"""
Name: CloudSign.Utils
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2026-06-24
LastEditTime: 2026-06-24
"""
from .client import CloudSignClient, generate_signature

__all__ = ['CloudSignClient', 'generate_signature', 'get_config']


def get_config():
    from nonebot import get_plugin_config
    from .config import Config
    return get_plugin_config(Config)
