# UnibeeInternalLogicGatewayRoPlanDetailRo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_ids** | **List[int]** | AddonIds | [optional] 
**addons** | [**List[UnibeeInternalLogicGatewayRoPlanSimplify]**](UnibeeInternalLogicGatewayRoPlanSimplify.md) | Addons | [optional] 
**metric_plan_limits** | [**List[UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo]**](UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo.md) | MetricPlanLimits | [optional] 
**plan** | [**UnibeeInternalLogicGatewayRoPlanSimplify**](UnibeeInternalLogicGatewayRoPlanSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_plan_detail_ro import UnibeeInternalLogicGatewayRoPlanDetailRo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoPlanDetailRo from a JSON string
unibee_internal_logic_gateway_ro_plan_detail_ro_instance = UnibeeInternalLogicGatewayRoPlanDetailRo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoPlanDetailRo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_plan_detail_ro_dict = unibee_internal_logic_gateway_ro_plan_detail_ro_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoPlanDetailRo from a dict
unibee_internal_logic_gateway_ro_plan_detail_ro_form_dict = unibee_internal_logic_gateway_ro_plan_detail_ro.from_dict(unibee_internal_logic_gateway_ro_plan_detail_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


