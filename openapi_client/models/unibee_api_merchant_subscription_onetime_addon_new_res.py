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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_bean_invoice_simplify import UnibeeApiBeanInvoiceSimplify
from openapi_client.models.unibee_api_bean_subscription_onetime_addon_simplify import UnibeeApiBeanSubscriptionOnetimeAddonSimplify
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantSubscriptionOnetimeAddonNewRes(BaseModel):
    """
    UnibeeApiMerchantSubscriptionOnetimeAddonNewRes
    """ # noqa: E501
    invoice: Optional[UnibeeApiBeanInvoiceSimplify] = None
    link: Optional[StrictStr] = Field(default=None, description="if automatic payment is false, Gateway Link will provided that manual payment needed")
    paid: Optional[StrictBool] = Field(default=None, description="true|false,automatic payment is default behavior for one-time addon purchased, payment will create attach to the purchase, when payment is success, return false, otherwise false")
    subscription_onetime_addon: Optional[UnibeeApiBeanSubscriptionOnetimeAddonSimplify] = Field(default=None, alias="subscriptionOnetimeAddon")
    __properties: ClassVar[List[str]] = ["invoice", "link", "paid", "subscriptionOnetimeAddon"]

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
        """Create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invoice
        if self.invoice:
            _dict['invoice'] = self.invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscription_onetime_addon
        if self.subscription_onetime_addon:
            _dict['subscriptionOnetimeAddon'] = self.subscription_onetime_addon.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoice": UnibeeApiBeanInvoiceSimplify.from_dict(obj["invoice"]) if obj.get("invoice") is not None else None,
            "link": obj.get("link"),
            "paid": obj.get("paid"),
            "subscriptionOnetimeAddon": UnibeeApiBeanSubscriptionOnetimeAddonSimplify.from_dict(obj["subscriptionOnetimeAddon"]) if obj.get("subscriptionOnetimeAddon") is not None else None
        })
        return _obj

