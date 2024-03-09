# UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[UnibeeInternalLogicGatewayRoPlanAddonVo]**](UnibeeInternalLogicGatewayRoPlanAddonVo.md) | Addon | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**period_end** | **int** | period_end | [optional] 
**period_end_time** | **str** | period end (datatime) | [optional] 
**period_start** | **int** | period_start | [optional] 
**period_start_time** | **str** | period start (datetime) | [optional] 
**plan** | [**UnibeeInternalLogicGatewayRoPlanSimplify**](UnibeeInternalLogicGatewayRoPlanSimplify.md) |  | [optional] 
**plan_id** | **int** | PlanId | [optional] 
**quantity** | **int** | quantity | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**unique_id** | **str** | unique id | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo import UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo from a JSON string
unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo_instance = UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo_dict = unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo from a dict
unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo_form_dict = unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo.from_dict(unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


