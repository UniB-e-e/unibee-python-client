# UnibeeApiMerchantWebhookNewEndpointReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[str]** | Events | [optional] 
**url** | **str** | Url | 

## Example

```python
from openapi_client.models.unibee_api_merchant_webhook_new_endpoint_req import UnibeeApiMerchantWebhookNewEndpointReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantWebhookNewEndpointReq from a JSON string
unibee_api_merchant_webhook_new_endpoint_req_instance = UnibeeApiMerchantWebhookNewEndpointReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantWebhookNewEndpointReq.to_json()

# convert the object into a dict
unibee_api_merchant_webhook_new_endpoint_req_dict = unibee_api_merchant_webhook_new_endpoint_req_instance.to_dict()
# create an instance of UnibeeApiMerchantWebhookNewEndpointReq from a dict
unibee_api_merchant_webhook_new_endpoint_req_form_dict = unibee_api_merchant_webhook_new_endpoint_req.from_dict(unibee_api_merchant_webhook_new_endpoint_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


