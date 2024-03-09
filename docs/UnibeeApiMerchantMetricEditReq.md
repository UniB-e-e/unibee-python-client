# UnibeeApiMerchantMetricEditReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_description** | **str** | MetricDescription | [optional] 
**metric_id** | **int** | MetricId | 
**metric_name** | **str** | MetricName | 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_edit_req import UnibeeApiMerchantMetricEditReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricEditReq from a JSON string
unibee_api_merchant_metric_edit_req_instance = UnibeeApiMerchantMetricEditReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricEditReq.to_json()

# convert the object into a dict
unibee_api_merchant_metric_edit_req_dict = unibee_api_merchant_metric_edit_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricEditReq from a dict
unibee_api_merchant_metric_edit_req_form_dict = unibee_api_merchant_metric_edit_req.from_dict(unibee_api_merchant_metric_edit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


