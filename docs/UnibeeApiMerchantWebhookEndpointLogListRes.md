# UnibeeApiMerchantWebhookEndpointLogListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_log_list** | [**List[UnibeeApiBeanMerchantWebhookLogSimplify]**](UnibeeApiBeanMerchantWebhookLogSimplify.md) | EndpointLogList | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_webhook_endpoint_log_list_res import UnibeeApiMerchantWebhookEndpointLogListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantWebhookEndpointLogListRes from a JSON string
unibee_api_merchant_webhook_endpoint_log_list_res_instance = UnibeeApiMerchantWebhookEndpointLogListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantWebhookEndpointLogListRes.to_json()

# convert the object into a dict
unibee_api_merchant_webhook_endpoint_log_list_res_dict = unibee_api_merchant_webhook_endpoint_log_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantWebhookEndpointLogListRes from a dict
unibee_api_merchant_webhook_endpoint_log_list_res_form_dict = unibee_api_merchant_webhook_endpoint_log_list_res.from_dict(unibee_api_merchant_webhook_endpoint_log_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


