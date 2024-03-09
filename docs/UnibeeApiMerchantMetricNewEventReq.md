# UnibeeApiMerchantMetricNewEventReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_event_id** | **str** | ExternalEventId, __unique__ | 
**external_user_id** | **str** | ExternalUserId | 
**metric_code** | **str** | MetricCode | 
**metric_properties** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_new_event_req import UnibeeApiMerchantMetricNewEventReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricNewEventReq from a JSON string
unibee_api_merchant_metric_new_event_req_instance = UnibeeApiMerchantMetricNewEventReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricNewEventReq.to_json()

# convert the object into a dict
unibee_api_merchant_metric_new_event_req_dict = unibee_api_merchant_metric_new_event_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricNewEventReq from a dict
unibee_api_merchant_metric_new_event_req_form_dict = unibee_api_merchant_metric_new_event_req.from_dict(unibee_api_merchant_metric_new_event_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


