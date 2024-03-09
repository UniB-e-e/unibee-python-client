# UnibeeInternalLogicGatewayRoMetricLimitVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** |  | [optional] 
**metric_id** | **int** |  | [optional] 
**plan_limits** | [**List[UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo]**](UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo.md) |  | [optional] 
**total_limit** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**aggregation_property** | **str** | aggregation property | [optional] 
**aggregation_type** | **int** | 0-count，1-count unique, 2-latest, 3-max, 4-sum | [optional] 
**code** | **str** | code | [optional] 
**metric_name** | **str** | metric name | [optional] 
**type** | **int** | 1-limit_metered，2-charge_metered(come later),3-charge_recurring(come later) | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_metric_limit_vo import UnibeeInternalLogicGatewayRoMetricLimitVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoMetricLimitVo from a JSON string
unibee_internal_logic_gateway_ro_metric_limit_vo_instance = UnibeeInternalLogicGatewayRoMetricLimitVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoMetricLimitVo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_metric_limit_vo_dict = unibee_internal_logic_gateway_ro_metric_limit_vo_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoMetricLimitVo from a dict
unibee_internal_logic_gateway_ro_metric_limit_vo_form_dict = unibee_internal_logic_gateway_ro_metric_limit_vo.from_dict(unibee_internal_logic_gateway_ro_metric_limit_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


