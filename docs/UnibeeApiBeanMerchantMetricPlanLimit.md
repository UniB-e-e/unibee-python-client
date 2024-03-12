# UnibeeApiBeanMerchantMetricPlanLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**gmt_modify** | **int** | update time | [optional] 
**id** | **int** | id | [optional] 
**merchant_id** | **int** | merchantId | [optional] 
**merchant_metric_vo** | [**UnibeeApiBeanMerchantMetricSimplify**](UnibeeApiBeanMerchantMetricSimplify.md) |  | [optional] 
**metric_id** | **int** | metricId | [optional] 
**metric_limit** | **int** | plan metric limit | [optional] 
**plan_id** | **int** | plan_id | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_metric_plan_limit import UnibeeApiBeanMerchantMetricPlanLimit

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantMetricPlanLimit from a JSON string
unibee_api_bean_merchant_metric_plan_limit_instance = UnibeeApiBeanMerchantMetricPlanLimit.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantMetricPlanLimit.to_json()

# convert the object into a dict
unibee_api_bean_merchant_metric_plan_limit_dict = unibee_api_bean_merchant_metric_plan_limit_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantMetricPlanLimit from a dict
unibee_api_bean_merchant_metric_plan_limit_form_dict = unibee_api_bean_merchant_metric_plan_limit.from_dict(unibee_api_bean_merchant_metric_plan_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


