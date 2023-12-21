from pydantic import BaseModel
from typing import Optional


class Refresh_Token_Response(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str
    scope: str
    token_type: str


class Refresh_Token_Payload(BaseModel):
    client_id: str
    client_secret: str
    grant_type: Optional[str] = "refresh_token"
    refresh_token: str


class ErrorToken(BaseModel):
    status: int
    error: str
    error_description: str
