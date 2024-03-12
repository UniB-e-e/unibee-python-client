# UnibeeApiBeanMerchantWebhookEndpointSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**gmt_modify** | **int** | update time | [optional] 
**id** | **int** | id | [optional] 
**merchant_id** | **int** | webhook url | [optional] 
**webhook_events** | **List[str]** | webhook_events,split dot | [optional] 
**webhook_url** | **str** | webhook url | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_webhook_endpoint_simplify import UnibeeApiBeanMerchantWebhookEndpointSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantWebhookEndpointSimplify from a JSON string
unibee_api_bean_merchant_webhook_endpoint_simplify_instance = UnibeeApiBeanMerchantWebhookEndpointSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantWebhookEndpointSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_webhook_endpoint_simplify_dict = unibee_api_bean_merchant_webhook_endpoint_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantWebhookEndpointSimplify from a dict
unibee_api_bean_merchant_webhook_endpoint_simplify_form_dict = unibee_api_bean_merchant_webhook_endpoint_simplify.from_dict(unibee_api_bean_merchant_webhook_endpoint_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


