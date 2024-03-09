# UnibeeInternalLogicGatewayRoInvoiceDetailSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_name** | **str** |  | [optional] 
**lines** | [**List[UnibeeInternalLogicGatewayRoInvoiceItemDetailRo]**](UnibeeInternalLogicGatewayRoInvoiceItemDetailRo.md) |  | [optional] 
**period_end** | **int** |  | [optional] 
**period_start** | **int** |  | [optional] 
**proration_date** | **int** |  | [optional] 
**proration_scale** | **int** |  | [optional] 
**subscription_amount** | **int** |  | [optional] 
**subscription_amount_excluding_tax** | **int** |  | [optional] 
**tax_amount** | **int** |  | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**total_amount** | **int** |  | [optional] 
**total_amount_excluding_tax** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_invoice_detail_simplify import UnibeeInternalLogicGatewayRoInvoiceDetailSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailSimplify from a JSON string
unibee_internal_logic_gateway_ro_invoice_detail_simplify_instance = UnibeeInternalLogicGatewayRoInvoiceDetailSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoInvoiceDetailSimplify.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_invoice_detail_simplify_dict = unibee_internal_logic_gateway_ro_invoice_detail_simplify_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailSimplify from a dict
unibee_internal_logic_gateway_ro_invoice_detail_simplify_form_dict = unibee_internal_logic_gateway_ro_invoice_detail_simplify.from_dict(unibee_internal_logic_gateway_ro_invoice_detail_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


