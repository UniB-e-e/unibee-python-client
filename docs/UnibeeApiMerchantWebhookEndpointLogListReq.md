# UnibeeApiMerchantWebhookEndpointLogListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**endpoint_id** | **int** | EndpointId | 
**page** | **int** | Page, Start WIth 0 | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_webhook_endpoint_log_list_req import UnibeeApiMerchantWebhookEndpointLogListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantWebhookEndpointLogListReq from a JSON string
unibee_api_merchant_webhook_endpoint_log_list_req_instance = UnibeeApiMerchantWebhookEndpointLogListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantWebhookEndpointLogListReq.to_json()

# convert the object into a dict
unibee_api_merchant_webhook_endpoint_log_list_req_dict = unibee_api_merchant_webhook_endpoint_log_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantWebhookEndpointLogListReq from a dict
unibee_api_merchant_webhook_endpoint_log_list_req_form_dict = unibee_api_merchant_webhook_endpoint_log_list_req.from_dict(unibee_api_merchant_webhook_endpoint_log_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


