# UnibeeInternalLogicWebhookMerchantWebhookEndpointVo


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
from openapi_client.models.unibee_internal_logic_webhook_merchant_webhook_endpoint_vo import UnibeeInternalLogicWebhookMerchantWebhookEndpointVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicWebhookMerchantWebhookEndpointVo from a JSON string
unibee_internal_logic_webhook_merchant_webhook_endpoint_vo_instance = UnibeeInternalLogicWebhookMerchantWebhookEndpointVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicWebhookMerchantWebhookEndpointVo.to_json()

# convert the object into a dict
unibee_internal_logic_webhook_merchant_webhook_endpoint_vo_dict = unibee_internal_logic_webhook_merchant_webhook_endpoint_vo_instance.to_dict()
# create an instance of UnibeeInternalLogicWebhookMerchantWebhookEndpointVo from a dict
unibee_internal_logic_webhook_merchant_webhook_endpoint_vo_form_dict = unibee_internal_logic_webhook_merchant_webhook_endpoint_vo.from_dict(unibee_internal_logic_webhook_merchant_webhook_endpoint_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


