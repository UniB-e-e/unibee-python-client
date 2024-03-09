# UnibeeApiMerchantMetricNewPlanLimitReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_id** | **int** | MetricId | 
**metric_limit** | **int** | MetricLimit | 
**plan_id** | **int** | PlanId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_new_plan_limit_req import UnibeeApiMerchantMetricNewPlanLimitReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricNewPlanLimitReq from a JSON string
unibee_api_merchant_metric_new_plan_limit_req_instance = UnibeeApiMerchantMetricNewPlanLimitReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricNewPlanLimitReq.to_json()

# convert the object into a dict
unibee_api_merchant_metric_new_plan_limit_req_dict = unibee_api_merchant_metric_new_plan_limit_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricNewPlanLimitReq from a dict
unibee_api_merchant_metric_new_plan_limit_req_form_dict = unibee_api_merchant_metric_new_plan_limit_req.from_dict(unibee_api_merchant_metric_new_plan_limit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


