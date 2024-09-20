'''
Name: CloudSign.Config
Author: Monarchdos <monarchdosw@gmail.com>
Date: 2024-07-14 17:37:27
LastEditTime: 2024-09-20 10:33:09
'''
from pydantic import BaseModel, field_validator

class Config(BaseModel):
    cloudsign_key: str = ""
    cloudsign_master: str = ""
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

    @field_validator('cloudsign_key', mode='before')
    def validate_cloudsign_key(cls, v):
        if v and (len(v) != 16 or not re.match(r'^[a-zA-Z0-9]+$', v)):
            raise ValueError('cloudsign_key must be 16 alphanumeric characters')
        return v

    @field_validator('cloudsign_master', mode='before')
    def validate_cloudsign_master(cls, v):
        if v and (len(v) >= 11 or not v.isdigit()):
            raise ValueError('cloudsign_master must be less than 11 digits')
        return v
