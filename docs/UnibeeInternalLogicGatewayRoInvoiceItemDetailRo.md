# UnibeeInternalLogicGatewayRoInvoiceItemDetailRo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**amount_excluding_tax** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**period_end** | **int** |  | [optional] 
**period_start** | **int** |  | [optional] 
**proration** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**unit_amount_excluding_tax** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_invoice_item_detail_ro import UnibeeInternalLogicGatewayRoInvoiceItemDetailRo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoInvoiceItemDetailRo from a JSON string
unibee_internal_logic_gateway_ro_invoice_item_detail_ro_instance = UnibeeInternalLogicGatewayRoInvoiceItemDetailRo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoInvoiceItemDetailRo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_invoice_item_detail_ro_dict = unibee_internal_logic_gateway_ro_invoice_item_detail_ro_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoInvoiceItemDetailRo from a dict
unibee_internal_logic_gateway_ro_invoice_item_detail_ro_form_dict = unibee_internal_logic_gateway_ro_invoice_item_detail_ro.from_dict(unibee_internal_logic_gateway_ro_invoice_item_detail_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


