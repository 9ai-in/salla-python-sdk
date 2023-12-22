from typing import Optional, Union

from pydantic import BaseModel, HttpUrl


#!------------------------------------------- MERCHANT SCHEMA -------------------------------------------------------
class Merchant(BaseModel):
    id: int
    username: str
    name: str
    avatar: Union[str, None]
    store_location: Union[str, None]
    plan: str
    status: str
    domain: Union[HttpUrl, str, None]
    tax_number: Union[str, None]
    commercial_number: Union[str, None]
    created_at: str


class UserData(BaseModel):
    id: int
    name: str
    email: str
    mobile: str
    role: str
    created_at: str
    merchant: Optional[Merchant] = None


class MerchantInfo(BaseModel):
    status: int
    success: bool
    data: UserData


#!------------------------------------------- STORE SCHEMA ---------------------------------------------------------
class Licenses(BaseModel):
    tax_number: Union[str, None]
    commercial_number: Union[str, None]
    freelance_number: Union[str, None]


class Social(BaseModel):
    telegram: Union[HttpUrl, None, str]
    twitter: Union[HttpUrl, None, str]
    facebook: Union[HttpUrl, None, str]
    maroof: Union[HttpUrl, None, str]
    youtube: Union[HttpUrl, None, str]
    snapchat: Union[HttpUrl, None, str]
    whatsapp: Union[str, None]
    appstore_link: Union[HttpUrl, None, str]
    googleplay_link: Union[HttpUrl, None, str]


class CompanyData(BaseModel):
    id: int
    name: str
    entity: str
    email: str
    avatar: Union[str, None]
    plan: str
    status: str
    verified: bool
    currency: str
    domain: Union[HttpUrl, None, str]
    description: str
    licenses: Licenses
    social: Social


class StoreInfo(BaseModel):
    status: int
    success: bool
    data: CompanyData
