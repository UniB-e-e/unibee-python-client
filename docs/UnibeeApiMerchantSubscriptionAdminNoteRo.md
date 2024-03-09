# UnibeeApiMerchantSubscriptionAdminNoteRo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | 邮箱 | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **int** | id | [optional] 
**last_name** | **str** |  | [optional] 
**mobile** | **str** | 手机号 | [optional] 
**note** | **str** | note | [optional] 
**subscription_id** | **str** | SubscriptionId | [optional] 
**user_name** | **str** | 用户名 | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_admin_note_ro import UnibeeApiMerchantSubscriptionAdminNoteRo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionAdminNoteRo from a JSON string
unibee_api_merchant_subscription_admin_note_ro_instance = UnibeeApiMerchantSubscriptionAdminNoteRo.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionAdminNoteRo.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_admin_note_ro_dict = unibee_api_merchant_subscription_admin_note_ro_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionAdminNoteRo from a dict
unibee_api_merchant_subscription_admin_note_ro_form_dict = unibee_api_merchant_subscription_admin_note_ro.from_dict(unibee_api_merchant_subscription_admin_note_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


