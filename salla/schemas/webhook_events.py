from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Literal


class Webhook_Events(Enum):
    #! ORDER
    ORDER_CREATED = "order.created"
    ORDER_UPDATED = "order.updated"
    ORDER_STATUS_UPDATED = "order.status.updated"
    ORDER_CANCELLED = "order.cancelled"
    ORDER_REFUNDED = "order.refunded"
    ORDER_DELETED = "order.deleted"
    ORDER_PRODUCTS_UPDATED = "order.products.updated"
    ORDER_PAYMENT_UPDATED = "order.payment.updated"
    ORDER_COUPON_UPDATED = "order.coupon.updated"
    ORDER_TOTAL_PRICE_UPDATED = "order.total.price.updated"
    ORDER_SHIPMENT_CREATING = "order.shipment.creating"
    ORDER_SHIPMENT_CREATED = "order.shipment.created"
    ORDER_SHIPMENT_CANCELLED = "order.shipment.cancelled"
    ORDER_SHIPMENT_RETURN_CREATING = (
        "order.shipment.return.creating"
    )
    ORDER_SHIPMENT_RETURN_CREATED = (
        "order.shipment.return.created"
    )
    ORDER_SHIPMENT_RETURN_CANCELLED = (
        "order.shipment.return.cancelled"
    )
    ORDER_SHIPPING_ADDRESS_UPDATED = (
        "order.shipping.address.updated"
    )

    #! PRODUCT
    PRODUCT_CREATED = "product.created"
    PRODUCT_UPDATED = "product.updated"
    PRODUCT_DELETED = "product.deleted"
    PRODUCT_AVAILABLE = "product.available"
    PRODUCT_QUANTITY_LOW = "product.quantity.low"

    #! SHIPPING COMPANIES
    SHIPPING_ZONE_CREATED = "shipping.zone.created"
    SHIPPING_ZONE_UPDATED = "shipping.zone.updated"
    SHIPPING_COMPANY_CREATED = "shipping.company.created"
    SHIPPING_COMPANY_UPDATED = "shipping.company.updated"
    SHIPPING_COMPANY_DELETED = "shipping.company.deleted"

    #! SHIPMENTS
    SHIPMENT_CREATING = "shipment.creating"
    SHIPMENT_CREATED = "shipment.created"
    SHIPMENT_CANCELLED = "shipment.cancelled"
    SHIPMENT_UPDATED = "shipment.updated"

    #! CUSTOMER
    CUSTOMER_CREATED = "customer.created"
    CUSTOMER_UPDATED = "customer.updated"
    CUSTOMER_LOGIN = "customer.login"
    CUSTOMER_OTP_REQUEST = "customer.otp.request"

    #! CATEGORY
    CATEGORY_CREATED = "category.created"
    CATEGORY_UPDATED = "category.updated"

    #! BRAND
    BRAND_CREATED = "brand.created"
    BRAND_UPDATED = "brand.updated"
    BRAND_DELETED = "brand.deleted"

    #! STORE
    STORE_BRANCH_CREATED = "store.branch.created"
    STORE_BRANCH_UPDATED = "store.branch.updated"
    STORE_BRANCH_SETDEFAULT = "store.branch.setDefault"
    STORE_BRANCH_ACTIVATED = "store.branch.activated"
    STORE_BRANCH_DELETED = "store.branch.deleted"
    STORETAX_CREATED = "storetax.created"

    #! CART
    ABANDONED_CART = "abandoned.cart"
    COUPON_APPLIED = "coupon.applied"

    #! INVOICE
    INVOICE_CREATED = "invoice.created"

    #! SPECIAL OFFERS
    SPECIALOFFER_CREATED = "specialoffer.created"
    SPECIALOFFER_UPDATED = "specialoffer.updated"

    #! MISCELLANEOUS
    REVIEW_ADDED = "review.added"


class SecurityConfig(BaseModel):
    strategy: str
    secret: str


class WebhookData(BaseModel):
    id: int
    name: str
    event: str
    version: str
    rule: Optional[str] = None
    url: str
    headers: List[str]
    security: SecurityConfig


class WebhookResponse(BaseModel):
    status: int
    success: bool
    data: WebhookData

    class Config:
        schema_extra = {
            "status": 200,
            "success": True,
            "data": {
                "id": 3423412,
                "name": "Order Updated Webhook with Payment",
                "event": "order.updated",
                "version": "2",
                "rule": "payment_method = mada",
                "url": "https://xxxxxx.app/webhook",
                "headers": [],
                "security": {
                    "strategy": "token",
                    "secret": "most_secure_key",
                },
            },
        }


class WebhookPayload(BaseModel):
    name: str
    event: Webhook_Events
    version: Optional[str] = "2"
    rule: Optional[str] = None
    url: str
    security_strategy: Literal["signature", "token", "none"]
    secret: str

    class Config:
        use_enum_values = True
        schema_extra = {
            "name": "Order Updated Webhook with Payment",
            "event": "order.updated",
            "version": "2",
            "rule": "payment_method = mada",
            "url": "https://webhook.site/168eb569-cbc5-40ad-8940-3dcd80xxx",
            "security_strategy": "signature",
            "secret": "ac3ea83628cccf2e98afc34223e4eeb5b41800b77737938aeed4exxx",
        }
