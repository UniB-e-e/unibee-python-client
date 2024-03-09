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
from openapi_client.models.unibee_api_system_information_support_currency import UnibeeApiSystemInformationSupportCurrency
from openapi_client.models.unibee_internal_logic_gateway_ro_gateway_simplify import UnibeeInternalLogicGatewayRoGatewaySimplify
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiSystemInformationGetRes(BaseModel):
    """
    UnibeeApiSystemInformationGetRes
    """ # noqa: E501
    env: Optional[StrictStr] = Field(default=None, description="System Env, em: daily|stage|local|prod")
    gateway: Optional[List[UnibeeInternalLogicGatewayRoGatewaySimplify]] = Field(default=None, description="Support Currency List")
    is_prod: Optional[StrictBool] = Field(default=None, description="Check System Env Is Prod, true|false", alias="isProd")
    support_currency: Optional[List[UnibeeApiSystemInformationSupportCurrency]] = Field(default=None, description="Support Currency List", alias="supportCurrency")
    support_time_zone: Optional[List[StrictStr]] = Field(default=None, description="Support TimeZone List", alias="supportTimeZone")
    __properties: ClassVar[List[str]] = ["env", "gateway", "isProd", "supportCurrency", "supportTimeZone"]

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
        """Create an instance of UnibeeApiSystemInformationGetRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in gateway (list)
        _items = []
        if self.gateway:
            for _item in self.gateway:
                if _item:
                    _items.append(_item.to_dict())
            _dict['gateway'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in support_currency (list)
        _items = []
        if self.support_currency:
            for _item in self.support_currency:
                if _item:
                    _items.append(_item.to_dict())
            _dict['supportCurrency'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiSystemInformationGetRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "env": obj.get("env"),
            "gateway": [UnibeeInternalLogicGatewayRoGatewaySimplify.from_dict(_item) for _item in obj["gateway"]] if obj.get("gateway") is not None else None,
            "isProd": obj.get("isProd"),
            "supportCurrency": [UnibeeApiSystemInformationSupportCurrency.from_dict(_item) for _item in obj["supportCurrency"]] if obj.get("supportCurrency") is not None else None,
            "supportTimeZone": obj.get("supportTimeZone")
        })
        return _obj

