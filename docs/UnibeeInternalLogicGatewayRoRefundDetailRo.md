# UnibeeInternalLogicGatewayRoRefundDetailRo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**UnibeeInternalLogicGatewayRoPaymentSimplify**](UnibeeInternalLogicGatewayRoPaymentSimplify.md) |  | [optional] 
**refund** | [**UnibeeInternalLogicGatewayRoRefundSimplify**](UnibeeInternalLogicGatewayRoRefundSimplify.md) |  | [optional] 
**user** | [**UnibeeInternalLogicGatewayRoUserAccountSimplify**](UnibeeInternalLogicGatewayRoUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_refund_detail_ro import UnibeeInternalLogicGatewayRoRefundDetailRo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoRefundDetailRo from a JSON string
unibee_internal_logic_gateway_ro_refund_detail_ro_instance = UnibeeInternalLogicGatewayRoRefundDetailRo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoRefundDetailRo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_refund_detail_ro_dict = unibee_internal_logic_gateway_ro_refund_detail_ro_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoRefundDetailRo from a dict
unibee_internal_logic_gateway_ro_refund_detail_ro_form_dict = unibee_internal_logic_gateway_ro_refund_detail_ro.from_dict(unibee_internal_logic_gateway_ro_refund_detail_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


