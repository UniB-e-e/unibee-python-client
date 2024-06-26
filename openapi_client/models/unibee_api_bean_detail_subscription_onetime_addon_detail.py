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
from openapi_client.models.unibee_api_bean_payment_simplify import UnibeeApiBeanPaymentSimplify
from openapi_client.models.unibee_api_bean_plan_simplify import UnibeeApiBeanPlanSimplify
from openapi_client.models.unibee_api_bean_user_account_simplify import UnibeeApiBeanUserAccountSimplify
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail(BaseModel):
    """
    UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail
    """ # noqa: E501
    addon: Optional[UnibeeApiBeanPlanSimplify] = None
    addon_id: Optional[StrictInt] = Field(default=None, description="onetime addonId", alias="addonId")
    create_time: Optional[StrictInt] = Field(default=None, description="create utc time", alias="createTime")
    id: Optional[StrictInt] = Field(default=None, description="id")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Metadata")
    payment: Optional[UnibeeApiBeanPaymentSimplify] = None
    quantity: Optional[StrictInt] = Field(default=None, description="quantity")
    status: Optional[StrictInt] = Field(default=None, description="status, 1-create, 2-paid, 3-cancel, 4-expired")
    subscription_id: Optional[StrictStr] = Field(default=None, description="subscription_id", alias="subscriptionId")
    user: Optional[UnibeeApiBeanUserAccountSimplify] = None
    __properties: ClassVar[List[str]] = ["addon", "addonId", "createTime", "id", "metadata", "payment", "quantity", "status", "subscriptionId", "user"]

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
        """Create an instance of UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of addon
        if self.addon:
            _dict['addon'] = self.addon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addon": UnibeeApiBeanPlanSimplify.from_dict(obj["addon"]) if obj.get("addon") is not None else None,
            "addonId": obj.get("addonId"),
            "createTime": obj.get("createTime"),
            "id": obj.get("id"),
            "metadata": obj.get("metadata"),
            "payment": UnibeeApiBeanPaymentSimplify.from_dict(obj["payment"]) if obj.get("payment") is not None else None,
            "quantity": obj.get("quantity"),
            "status": obj.get("status"),
            "subscriptionId": obj.get("subscriptionId"),
            "user": UnibeeApiBeanUserAccountSimplify.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


