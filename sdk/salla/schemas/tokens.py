from typing import Dict, Optional, Union

from pydantic import BaseModel


class Access_Token_Response(BaseModel):
    access_token: str
    expires_in: int
    refresh_token: str
    scope: str
    token_type: str


class Access_Token_Payload(BaseModel):
    client_id: str
    client_secret: str
    grant_type: Optional[str] = "authorization_code"
    code: str
    scope: Optional[str] = "offline_access"
    redirect_uri: Optional[str] = None


class Refresh_Token_Payload(BaseModel):
    client_id: str
    client_secret: str
    grant_type: Optional[str] = "refresh_token"
    refresh_token: str


class ErrorToken(BaseModel):
    status: Optional[int] = None
    success: Optional[bool] = None
    error: Union[Dict, str] = None
    error_description: Optional[str] = None
