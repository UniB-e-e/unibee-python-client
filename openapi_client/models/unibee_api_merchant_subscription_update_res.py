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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_bean_detail_subscription_pending_update_detail import UnibeeApiBeanDetailSubscriptionPendingUpdateDetail
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantSubscriptionUpdateRes(BaseModel):
    """
    UnibeeApiMerchantSubscriptionUpdateRes
    """ # noqa: E501
    link: Optional[StrictStr] = None
    paid: Optional[StrictBool] = None
    subscription_pending_update: Optional[UnibeeApiBeanDetailSubscriptionPendingUpdateDetail] = Field(default=None, alias="subscriptionPendingUpdate")
    __properties: ClassVar[List[str]] = ["link", "paid", "subscriptionPendingUpdate"]

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
        """Create an instance of UnibeeApiMerchantSubscriptionUpdateRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of subscription_pending_update
        if self.subscription_pending_update:
            _dict['subscriptionPendingUpdate'] = self.subscription_pending_update.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantSubscriptionUpdateRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "link": obj.get("link"),
            "paid": obj.get("paid"),
            "subscriptionPendingUpdate": UnibeeApiBeanDetailSubscriptionPendingUpdateDetail.from_dict(obj["subscriptionPendingUpdate"]) if obj.get("subscriptionPendingUpdate") is not None else None
        })
        return _obj


