# UnibeeApiMerchantSubscriptionAdminNoteListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**page** | **int** | Page, Start WIth 0 | [optional] 
**subscription_id** | **str** | SubscriptionId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_admin_note_list_req import UnibeeApiMerchantSubscriptionAdminNoteListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionAdminNoteListReq from a JSON string
unibee_api_merchant_subscription_admin_note_list_req_instance = UnibeeApiMerchantSubscriptionAdminNoteListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionAdminNoteListReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_admin_note_list_req_dict = unibee_api_merchant_subscription_admin_note_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionAdminNoteListReq from a dict
unibee_api_merchant_subscription_admin_note_list_req_form_dict = unibee_api_merchant_subscription_admin_note_list_req.from_dict(unibee_api_merchant_subscription_admin_note_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


