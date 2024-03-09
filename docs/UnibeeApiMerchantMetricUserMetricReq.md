# UnibeeApiMerchantMetricUserMetricReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_user_id** | **str** | ExternalUserId, One Of UserId|ExternalUserId Needed | [optional] 
**user_id** | **int** | UserId, One Of UserId|ExternalUserId Needed | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_user_metric_req import UnibeeApiMerchantMetricUserMetricReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricUserMetricReq from a JSON string
unibee_api_merchant_metric_user_metric_req_instance = UnibeeApiMerchantMetricUserMetricReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricUserMetricReq.to_json()

# convert the object into a dict
unibee_api_merchant_metric_user_metric_req_dict = unibee_api_merchant_metric_user_metric_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricUserMetricReq from a dict
unibee_api_merchant_metric_user_metric_req_form_dict = unibee_api_merchant_metric_user_metric_req.from_dict(unibee_api_merchant_metric_user_metric_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


