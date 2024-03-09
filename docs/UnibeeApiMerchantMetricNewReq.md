# UnibeeApiMerchantMetricNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_property** | **str** | AggregationProperty, Will Needed When AggregationType !&#x3D; count | [optional] 
**aggregation_type** | **int** | AggregationType,1-count，2-count unique, 3-latest, 4-max, 5-sum | [optional] 
**code** | **str** | Code | 
**metric_description** | **str** | MetricDescription | [optional] 
**metric_name** | **str** | MetricName | 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_new_req import UnibeeApiMerchantMetricNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricNewReq from a JSON string
unibee_api_merchant_metric_new_req_instance = UnibeeApiMerchantMetricNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_metric_new_req_dict = unibee_api_merchant_metric_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricNewReq from a dict
unibee_api_merchant_metric_new_req_form_dict = unibee_api_merchant_metric_new_req.from_dict(unibee_api_merchant_metric_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


