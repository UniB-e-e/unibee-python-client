# MerchantWebhookEndpointLogListGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_log_list** | [**List[UnibeeApiBeanMerchantWebhookLogSimplify]**](UnibeeApiBeanMerchantWebhookLogSimplify.md) | EndpointLogList | [optional] 

## Example

```python
from openapi_client.models.merchant_webhook_endpoint_log_list_get200_response_data import MerchantWebhookEndpointLogListGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantWebhookEndpointLogListGet200ResponseData from a JSON string
merchant_webhook_endpoint_log_list_get200_response_data_instance = MerchantWebhookEndpointLogListGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantWebhookEndpointLogListGet200ResponseData.to_json()

# convert the object into a dict
merchant_webhook_endpoint_log_list_get200_response_data_dict = merchant_webhook_endpoint_log_list_get200_response_data_instance.to_dict()
# create an instance of MerchantWebhookEndpointLogListGet200ResponseData from a dict
merchant_webhook_endpoint_log_list_get200_response_data_form_dict = merchant_webhook_endpoint_log_list_get200_response_data.from_dict(merchant_webhook_endpoint_log_list_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


