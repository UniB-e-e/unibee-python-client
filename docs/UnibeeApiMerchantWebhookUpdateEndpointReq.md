# UnibeeApiMerchantWebhookUpdateEndpointReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** | EndpointId | 
**events** | **List[str]** | Events To Update | [optional] 
**url** | **str** | Url To Update | 

## Example

```python
from openapi_client.models.unibee_api_merchant_webhook_update_endpoint_req import UnibeeApiMerchantWebhookUpdateEndpointReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantWebhookUpdateEndpointReq from a JSON string
unibee_api_merchant_webhook_update_endpoint_req_instance = UnibeeApiMerchantWebhookUpdateEndpointReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantWebhookUpdateEndpointReq.to_json()

# convert the object into a dict
unibee_api_merchant_webhook_update_endpoint_req_dict = unibee_api_merchant_webhook_update_endpoint_req_instance.to_dict()
# create an instance of UnibeeApiMerchantWebhookUpdateEndpointReq from a dict
unibee_api_merchant_webhook_update_endpoint_req_form_dict = unibee_api_merchant_webhook_update_endpoint_req.from_dict(unibee_api_merchant_webhook_update_endpoint_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


