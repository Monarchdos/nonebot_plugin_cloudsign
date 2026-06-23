'''
Name: CloudSign.Config
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2024-07-14 17:37:27
LastEditTime: 2026-06-23 21:30:15
'''
from pydantic import BaseModel, field_validator
from typing import Union

class Config(BaseModel):
    cloudsign_master: Union[str, int] = ""
    cloudsign_app_key: str = ""
    cloudsign_app_secret: str = ""
    cloudsign_reply_quote: bool = True
    cloudsign_reply_at: bool = False

    @field_validator('cloudsign_reply_quote', 'cloudsign_reply_at', mode='before')
    def check_reply_options(cls, v, info):
        if not isinstance(v, bool):
            raise ValueError(f"{info.field_name} must be a boolean")
        values = info.data
        if info.field_name == 'cloudsign_reply_quote' and v and values.get('cloudsign_reply_at'):
            raise ValueError('Cannot enable both cloudsign_reply_quote and cloudsign_reply_at at the same time')
        if info.field_name == 'cloudsign_reply_at' and v and values.get('cloudsign_reply_quote'):
            raise ValueError('Cannot enable both cloudsign_reply_at and cloudsign_reply_quote at the same time')
        return v
        
