# UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**gmt_modify** | **int** | update time | [optional] 
**id** | **int** | id | [optional] 
**merchant_id** | **int** | merchantId | [optional] 
**merchant_metric_vo** | [**UnibeeInternalLogicGatewayRoMerchantMetricVo**](UnibeeInternalLogicGatewayRoMerchantMetricVo.md) |  | [optional] 
**metric_id** | **int** | metricId | [optional] 
**metric_limit** | **int** | plan metric limit | [optional] 
**plan_id** | **int** | plan_id | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo import UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo from a JSON string
unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo_instance = UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo_dict = unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoMerchantMetricPlanLimitVo from a dict
unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo_form_dict = unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo.from_dict(unibee_internal_logic_gateway_ro_merchant_metric_plan_limit_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


