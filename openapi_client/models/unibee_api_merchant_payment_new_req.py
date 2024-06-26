# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_merchant_payment_item import UnibeeApiMerchantPaymentItem
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantPaymentNewReq(BaseModel):
    """
    UnibeeApiMerchantPaymentNewReq
    """ # noqa: E501
    country_code: Optional[StrictStr] = Field(default=None, description="CountryCode", alias="countryCode")
    currency: Optional[StrictStr] = Field(default=None, description="Currency, either Currency&TotalAmount or PlanId needed")
    email: Optional[StrictStr] = Field(default=None, description="Email, either ExternalUserId&Email or UserId needed")
    external_payment_id: Optional[StrictStr] = Field(default=None, description="ExternalPaymentId should unique for payment", alias="externalPaymentId")
    external_user_id: Optional[StrictStr] = Field(default=None, description="ExternalUserId, unique, either ExternalUserId&Email or UserId needed", alias="externalUserId")
    gas_payer: Optional[StrictStr] = Field(default=None, description="who pay the gas, merchant|user", alias="gasPayer")
    gateway_id: StrictInt = Field(description="GatewayId", alias="gatewayId")
    items: Optional[List[UnibeeApiMerchantPaymentItem]] = Field(default=None, description="Items")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Metadata，Map")
    plan_id: Optional[StrictInt] = Field(default=None, description="PlanId, either TotalAmount&Currency or PlanId needed", alias="planId")
    redirect_url: Optional[StrictStr] = Field(default=None, description="Redirect Url", alias="redirectUrl")
    total_amount: Optional[StrictInt] = Field(default=None, description="Total PaymentAmount, Cent, either TotalAmount&Currency or PlanId needed", alias="totalAmount")
    user_id: Optional[StrictInt] = Field(default=None, description="UserId, either ExternalUserId&Email or UserId needed", alias="userId")
    __properties: ClassVar[List[str]] = ["countryCode", "currency", "email", "externalPaymentId", "externalUserId", "gasPayer", "gatewayId", "items", "metadata", "planId", "redirectUrl", "totalAmount", "userId"]

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
        """Create an instance of UnibeeApiMerchantPaymentNewReq from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantPaymentNewReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "countryCode": obj.get("countryCode"),
            "currency": obj.get("currency"),
            "email": obj.get("email"),
            "externalPaymentId": obj.get("externalPaymentId"),
            "externalUserId": obj.get("externalUserId"),
            "gasPayer": obj.get("gasPayer"),
            "gatewayId": obj.get("gatewayId"),
            "items": [UnibeeApiMerchantPaymentItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "metadata": obj.get("metadata"),
            "planId": obj.get("planId"),
            "redirectUrl": obj.get("redirectUrl"),
            "totalAmount": obj.get("totalAmount"),
            "userId": obj.get("userId")
        })
        return _obj


