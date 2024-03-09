# UnibeeInternalModelEntityOverseaPayMerchantWebhookLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | body(json) | [optional] 
**create_time** | **int** | create utc time | [optional] 
**endpoint_id** | **int** |  | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
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
from openapi_client.models.unibee_internal_model_entity_oversea_pay_merchant_webhook_log import UnibeeInternalModelEntityOverseaPayMerchantWebhookLog

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayMerchantWebhookLog from a JSON string
unibee_internal_model_entity_oversea_pay_merchant_webhook_log_instance = UnibeeInternalModelEntityOverseaPayMerchantWebhookLog.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayMerchantWebhookLog.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_merchant_webhook_log_dict = unibee_internal_model_entity_oversea_pay_merchant_webhook_log_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayMerchantWebhookLog from a dict
unibee_internal_model_entity_oversea_pay_merchant_webhook_log_form_dict = unibee_internal_model_entity_oversea_pay_merchant_webhook_log.from_dict(unibee_internal_model_entity_oversea_pay_merchant_webhook_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


