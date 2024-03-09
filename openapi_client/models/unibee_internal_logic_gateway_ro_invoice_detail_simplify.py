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
from openapi_client.models.unibee_internal_logic_gateway_ro_invoice_item_detail_ro import UnibeeInternalLogicGatewayRoInvoiceItemDetailRo
from typing import Optional, Set
from typing_extensions import Self

class UnibeeInternalLogicGatewayRoInvoiceDetailSimplify(BaseModel):
    """
    UnibeeInternalLogicGatewayRoInvoiceDetailSimplify
    """ # noqa: E501
    currency: Optional[StrictStr] = None
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceId")
    invoice_name: Optional[StrictStr] = Field(default=None, alias="invoiceName")
    lines: Optional[List[UnibeeInternalLogicGatewayRoInvoiceItemDetailRo]] = None
    period_end: Optional[StrictInt] = Field(default=None, alias="periodEnd")
    period_start: Optional[StrictInt] = Field(default=None, alias="periodStart")
    proration_date: Optional[StrictInt] = Field(default=None, alias="prorationDate")
    proration_scale: Optional[StrictInt] = Field(default=None, alias="prorationScale")
    subscription_amount: Optional[StrictInt] = Field(default=None, alias="subscriptionAmount")
    subscription_amount_excluding_tax: Optional[StrictInt] = Field(default=None, alias="subscriptionAmountExcludingTax")
    tax_amount: Optional[StrictInt] = Field(default=None, alias="taxAmount")
    tax_scale: Optional[StrictInt] = Field(default=None, description="Tax Scale，1000 = 10%", alias="taxScale")
    total_amount: Optional[StrictInt] = Field(default=None, alias="totalAmount")
    total_amount_excluding_tax: Optional[StrictInt] = Field(default=None, alias="totalAmountExcludingTax")
    __properties: ClassVar[List[str]] = ["currency", "invoiceId", "invoiceName", "lines", "periodEnd", "periodStart", "prorationDate", "prorationScale", "subscriptionAmount", "subscriptionAmountExcludingTax", "taxAmount", "taxScale", "totalAmount", "totalAmountExcludingTax"]

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
        """Create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailSimplify from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailSimplify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currency": obj.get("currency"),
            "invoiceId": obj.get("invoiceId"),
            "invoiceName": obj.get("invoiceName"),
            "lines": [UnibeeInternalLogicGatewayRoInvoiceItemDetailRo.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "periodEnd": obj.get("periodEnd"),
            "periodStart": obj.get("periodStart"),
            "prorationDate": obj.get("prorationDate"),
            "prorationScale": obj.get("prorationScale"),
            "subscriptionAmount": obj.get("subscriptionAmount"),
            "subscriptionAmountExcludingTax": obj.get("subscriptionAmountExcludingTax"),
            "taxAmount": obj.get("taxAmount"),
            "taxScale": obj.get("taxScale"),
            "totalAmount": obj.get("totalAmount"),
            "totalAmountExcludingTax": obj.get("totalAmountExcludingTax")
        })
        return _obj

