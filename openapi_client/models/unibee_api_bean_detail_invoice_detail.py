# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_bean_gateway_simplify import UnibeeApiBeanGatewaySimplify
from openapi_client.models.unibee_api_bean_invoice_item_simplify import UnibeeApiBeanInvoiceItemSimplify
from openapi_client.models.unibee_api_bean_merchant_simplify import UnibeeApiBeanMerchantSimplify
from openapi_client.models.unibee_api_bean_payment_simplify import UnibeeApiBeanPaymentSimplify
from openapi_client.models.unibee_api_bean_refund_simplify import UnibeeApiBeanRefundSimplify
from openapi_client.models.unibee_api_bean_subscription_simplify import UnibeeApiBeanSubscriptionSimplify
from openapi_client.models.unibee_api_bean_user_account_simplify import UnibeeApiBeanUserAccountSimplify
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiBeanDetailInvoiceDetail(BaseModel):
    """
    UnibeeApiBeanDetailInvoiceDetail
    """ # noqa: E501
    crypto_amount: Optional[StrictInt] = Field(default=None, description="crypto_amount, cent", alias="cryptoAmount")
    crypto_currency: Optional[StrictStr] = Field(default=None, description="crypto_currency", alias="cryptoCurrency")
    currency: Optional[StrictStr] = Field(default=None, description="Currency")
    data: Optional[StrictStr] = Field(default=None, description="Data")
    day_util_due: Optional[StrictInt] = Field(default=None, description="day util due after finish", alias="dayUtilDue")
    discount_amount: Optional[StrictInt] = Field(default=None, description="DiscountAmount,Cents", alias="discountAmount")
    gateway: Optional[UnibeeApiBeanGatewaySimplify] = None
    gateway_id: Optional[StrictInt] = Field(default=None, description="Id", alias="gatewayId")
    gateway_invoice_id: Optional[StrictStr] = Field(default=None, description="GatewayInvoiceId", alias="gatewayInvoiceId")
    gateway_invoice_pdf: Optional[StrictStr] = Field(default=None, description="GatewayInvoicePdf pdf", alias="gatewayInvoicePdf")
    gateway_payment_id: Optional[StrictStr] = Field(default=None, description="GatewayPaymentId PaymentId", alias="gatewayPaymentId")
    gateway_status: Optional[StrictStr] = Field(default=None, description="GatewayStatus，Stripe：https://stripe.com/docs/api/invoices/object", alias="gatewayStatus")
    gateway_user_id: Optional[StrictStr] = Field(default=None, description="GatewayUserId Id", alias="gatewayUserId")
    gmt_create: Optional[StrictStr] = Field(default=None, description="GmtCreate", alias="gmtCreate")
    gmt_modify: Optional[StrictStr] = Field(default=None, description="GmtModify", alias="gmtModify")
    id: Optional[StrictInt] = None
    invoice_id: Optional[StrictStr] = Field(default=None, description="InvoiceId", alias="invoiceId")
    invoice_name: Optional[StrictStr] = Field(default=None, description="InvoiceName", alias="invoiceName")
    is_deleted: Optional[StrictInt] = Field(default=None, alias="isDeleted")
    lines: Optional[List[UnibeeApiBeanInvoiceItemSimplify]] = Field(default=None, description="lines json data")
    link: Optional[StrictStr] = Field(default=None, description="Link")
    merchant: Optional[UnibeeApiBeanMerchantSimplify] = None
    merchant_id: Optional[StrictInt] = Field(default=None, description="MerchantId", alias="merchantId")
    payment: Optional[UnibeeApiBeanPaymentSimplify] = None
    payment_id: Optional[StrictStr] = Field(default=None, description="PaymentId", alias="paymentId")
    period_end: Optional[StrictInt] = Field(default=None, description="period_end", alias="periodEnd")
    period_start: Optional[StrictInt] = Field(default=None, description="period_start", alias="periodStart")
    refund: Optional[UnibeeApiBeanRefundSimplify] = None
    refund_id: Optional[StrictStr] = Field(default=None, description="refundId", alias="refundId")
    send_email: Optional[StrictStr] = Field(default=None, description="SendEmail", alias="sendEmail")
    send_note: Optional[StrictStr] = Field(default=None, description="SendNote", alias="sendNote")
    send_pdf: Optional[StrictStr] = Field(default=None, description="SendPdf", alias="sendPdf")
    send_status: Optional[StrictInt] = Field(default=None, description="SendStatus，0-No | 1- YES", alias="sendStatus")
    send_terms: Optional[StrictStr] = Field(default=None, description="SendTerms", alias="sendTerms")
    status: Optional[StrictInt] = Field(default=None, description="Status，0-Init | 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled")
    subscription: Optional[UnibeeApiBeanSubscriptionSimplify] = None
    subscription_amount: Optional[StrictInt] = Field(default=None, description="SubscriptionAmount,Cents", alias="subscriptionAmount")
    subscription_amount_excluding_tax: Optional[StrictInt] = Field(default=None, description="SubscriptionAmountExcludingTax,Cents", alias="subscriptionAmountExcludingTax")
    subscription_id: Optional[StrictStr] = Field(default=None, description="SubscriptionId", alias="subscriptionId")
    tax_amount: Optional[StrictInt] = Field(default=None, description="TaxAmount,Cents", alias="taxAmount")
    tax_scale: Optional[StrictInt] = Field(default=None, description="TaxScale，1000 = 10%", alias="taxScale")
    total_amount: Optional[StrictInt] = Field(default=None, description="TotalAmount,Cents", alias="totalAmount")
    total_amount_excluding_tax: Optional[StrictInt] = Field(default=None, description="TotalAmountExcludingTax,Cents", alias="totalAmountExcludingTax")
    unique_id: Optional[StrictStr] = Field(default=None, description="UniqueId", alias="uniqueId")
    user_account: Optional[UnibeeApiBeanUserAccountSimplify] = Field(default=None, alias="userAccount")
    user_id: Optional[StrictInt] = Field(default=None, description="UserId", alias="userId")
    __properties: ClassVar[List[str]] = ["cryptoAmount", "cryptoCurrency", "currency", "data", "dayUtilDue", "discountAmount", "gateway", "gatewayId", "gatewayInvoiceId", "gatewayInvoicePdf", "gatewayPaymentId", "gatewayStatus", "gatewayUserId", "gmtCreate", "gmtModify", "id", "invoiceId", "invoiceName", "isDeleted", "lines", "link", "merchant", "merchantId", "payment", "paymentId", "periodEnd", "periodStart", "refund", "refundId", "sendEmail", "sendNote", "sendPdf", "sendStatus", "sendTerms", "status", "subscription", "subscriptionAmount", "subscriptionAmountExcludingTax", "subscriptionId", "taxAmount", "taxScale", "totalAmount", "totalAmountExcludingTax", "uniqueId", "userAccount", "userId"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UnibeeApiBeanDetailInvoiceDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of gateway
        if self.gateway:
            _dict['gateway'] = self.gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of merchant
        if self.merchant:
            _dict['merchant'] = self.merchant.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refund
        if self.refund:
            _dict['refund'] = self.refund.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_account
        if self.user_account:
            _dict['userAccount'] = self.user_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiBeanDetailInvoiceDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cryptoAmount": obj.get("cryptoAmount"),
            "cryptoCurrency": obj.get("cryptoCurrency"),
            "currency": obj.get("currency"),
            "data": obj.get("data"),
            "dayUtilDue": obj.get("dayUtilDue"),
            "discountAmount": obj.get("discountAmount"),
            "gateway": UnibeeApiBeanGatewaySimplify.from_dict(obj["gateway"]) if obj.get("gateway") is not None else None,
            "gatewayId": obj.get("gatewayId"),
            "gatewayInvoiceId": obj.get("gatewayInvoiceId"),
            "gatewayInvoicePdf": obj.get("gatewayInvoicePdf"),
            "gatewayPaymentId": obj.get("gatewayPaymentId"),
            "gatewayStatus": obj.get("gatewayStatus"),
            "gatewayUserId": obj.get("gatewayUserId"),
            "gmtCreate": obj.get("gmtCreate"),
            "gmtModify": obj.get("gmtModify"),
            "id": obj.get("id"),
            "invoiceId": obj.get("invoiceId"),
            "invoiceName": obj.get("invoiceName"),
            "isDeleted": obj.get("isDeleted"),
            "lines": [UnibeeApiBeanInvoiceItemSimplify.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "link": obj.get("link"),
            "merchant": UnibeeApiBeanMerchantSimplify.from_dict(obj["merchant"]) if obj.get("merchant") is not None else None,
            "merchantId": obj.get("merchantId"),
            "payment": UnibeeApiBeanPaymentSimplify.from_dict(obj["payment"]) if obj.get("payment") is not None else None,
            "paymentId": obj.get("paymentId"),
            "periodEnd": obj.get("periodEnd"),
            "periodStart": obj.get("periodStart"),
            "refund": UnibeeApiBeanRefundSimplify.from_dict(obj["refund"]) if obj.get("refund") is not None else None,
            "refundId": obj.get("refundId"),
            "sendEmail": obj.get("sendEmail"),
            "sendNote": obj.get("sendNote"),
            "sendPdf": obj.get("sendPdf"),
            "sendStatus": obj.get("sendStatus"),
            "sendTerms": obj.get("sendTerms"),
            "status": obj.get("status"),
            "subscription": UnibeeApiBeanSubscriptionSimplify.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "subscriptionAmount": obj.get("subscriptionAmount"),
            "subscriptionAmountExcludingTax": obj.get("subscriptionAmountExcludingTax"),
            "subscriptionId": obj.get("subscriptionId"),
            "taxAmount": obj.get("taxAmount"),
            "taxScale": obj.get("taxScale"),
            "totalAmount": obj.get("totalAmount"),
            "totalAmountExcludingTax": obj.get("totalAmountExcludingTax"),
            "uniqueId": obj.get("uniqueId"),
            "userAccount": UnibeeApiBeanUserAccountSimplify.from_dict(obj["userAccount"]) if obj.get("userAccount") is not None else None,
            "userId": obj.get("userId")
        })
        return _obj

