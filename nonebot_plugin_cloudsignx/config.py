'''
Name: CloudSign.Config
Author: Monarchdos
Date: 2024-07-14 17:37:27
LastEditTime: 2024-07-14 19:36:33
'''
from pydantic import BaseModel, validator

class Config(BaseModel):
    cloudsign_key: str = ""
    cloudsign_master: str = ""
    cloudsign_reply_at: bool = True

    @validator('cloudsign_reply_at', pre=True, always=True)
    def check_boolean(cls, v):
        if not isinstance(v, bool):
            raise ValueError('cloudsign_reply_at must be a boolean value')
        return v
        
    @validator('cloudsign_key', pre=True, always=True)
    def validate_cloudsign_key(cls, v):
        if v and (len(v) != 16 or not re.match(r'^[a-zA-Z0-9]+$', v)):
            raise ValueError('cloudsign_key must be 16 alphanumeric characters')
        return v

    @validator('cloudsign_master', pre=True, always=True)
    def validate_cloudsign_master(cls, v):
        if v and (len(v) >= 11 or not v.isdigit()):
            raise ValueError('cloudsign_master must be less than 11 digits')
        return v
