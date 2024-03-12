# UnibeeApiBeanMerchantWebhookLogSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | body(json) | [optional] 
**create_time** | **int** | create utc time | [optional] 
**endpoint_id** | **int** |  | [optional] 
**id** | **int** | id | [optional] 
**mamo** | **str** | mamo | [optional] 
**merchant_id** | **int** | webhook url | [optional] 
**reconsume_count** | **int** |  | [optional] 
**request_id** | **str** | request_id | [optional] 
**response** | **str** | response | [optional] 
**webhook_event** | **str** | webhook_event | [optional] 
**webhook_url** | **str** | webhook url | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_webhook_log_simplify import UnibeeApiBeanMerchantWebhookLogSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantWebhookLogSimplify from a JSON string
unibee_api_bean_merchant_webhook_log_simplify_instance = UnibeeApiBeanMerchantWebhookLogSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantWebhookLogSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_webhook_log_simplify_dict = unibee_api_bean_merchant_webhook_log_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantWebhookLogSimplify from a dict
unibee_api_bean_merchant_webhook_log_simplify_form_dict = unibee_api_bean_merchant_webhook_log_simplify.from_dict(unibee_api_bean_merchant_webhook_log_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


