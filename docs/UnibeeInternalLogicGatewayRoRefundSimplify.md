# UnibeeInternalLogicGatewayRoRefundSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | country code | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**external_refund_id** | **str** | external_refund_id | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_refund_id** | **str** | gateway refund id | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**payment_id** | **str** | relative payment id | [optional] 
**refund_amount** | **int** | refund amount, cent | [optional] 
**refund_comment** | **str** | refund comment | [optional] 
**refund_id** | **str** | refund id (system generate) | [optional] 
**refund_time** | **int** | refund success time | [optional] 
**return_url** | **str** | return url after refund success | [optional] 
**status** | **int** | status。10-pending，20-success，30-failure, 40-cancel | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**user_id** | **int** | user_id | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_refund_simplify import UnibeeInternalLogicGatewayRoRefundSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoRefundSimplify from a JSON string
unibee_internal_logic_gateway_ro_refund_simplify_instance = UnibeeInternalLogicGatewayRoRefundSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoRefundSimplify.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_refund_simplify_dict = unibee_internal_logic_gateway_ro_refund_simplify_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoRefundSimplify from a dict
unibee_internal_logic_gateway_ro_refund_simplify_form_dict = unibee_internal_logic_gateway_ro_refund_simplify.from_dict(unibee_internal_logic_gateway_ro_refund_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


