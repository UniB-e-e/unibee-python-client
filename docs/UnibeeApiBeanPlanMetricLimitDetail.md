# UnibeeApiBeanPlanMetricLimitDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **int** |  | [optional] 
**metric_id** | **int** |  | [optional] 
**plan_limits** | [**List[UnibeeApiBeanMerchantMetricPlanLimit]**](UnibeeApiBeanMerchantMetricPlanLimit.md) |  | [optional] 
**total_limit** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**aggregation_property** | **str** | aggregation property | [optional] 
**aggregation_type** | **int** | 0-count，1-count unique, 2-latest, 3-max, 4-sum | [optional] 
**code** | **str** | code | [optional] 
**metric_name** | **str** | metric name | [optional] 
**type** | **int** | 1-limit_metered，2-charge_metered(come later),3-charge_recurring(come later) | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_plan_metric_limit_detail import UnibeeApiBeanPlanMetricLimitDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPlanMetricLimitDetail from a JSON string
unibee_api_bean_plan_metric_limit_detail_instance = UnibeeApiBeanPlanMetricLimitDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPlanMetricLimitDetail.to_json()

# convert the object into a dict
unibee_api_bean_plan_metric_limit_detail_dict = unibee_api_bean_plan_metric_limit_detail_instance.to_dict()
# create an instance of UnibeeApiBeanPlanMetricLimitDetail from a dict
unibee_api_bean_plan_metric_limit_detail_form_dict = unibee_api_bean_plan_metric_limit_detail.from_dict(unibee_api_bean_plan_metric_limit_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


