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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_bean_detail_subscription_time_line_detail import UnibeeApiBeanDetailSubscriptionTimeLineDetail
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantSubscriptionTimeLineListRes(BaseModel):
    """
    UnibeeApiMerchantSubscriptionTimeLineListRes
    """ # noqa: E501
    subscription_time_lines: Optional[List[UnibeeApiBeanDetailSubscriptionTimeLineDetail]] = Field(default=None, description="SubscriptionTimeLines", alias="subscriptionTimeLines")
    __properties: ClassVar[List[str]] = ["subscriptionTimeLines"]

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
        """Create an instance of UnibeeApiMerchantSubscriptionTimeLineListRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in subscription_time_lines (list)
        _items = []
        if self.subscription_time_lines:
            for _item in self.subscription_time_lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subscriptionTimeLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantSubscriptionTimeLineListRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscriptionTimeLines": [UnibeeApiBeanDetailSubscriptionTimeLineDetail.from_dict(_item) for _item in obj["subscriptionTimeLines"]] if obj.get("subscriptionTimeLines") is not None else None
        })
        return _obj


