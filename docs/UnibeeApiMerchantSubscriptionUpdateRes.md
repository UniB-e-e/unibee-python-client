# UnibeeApiMerchantSubscriptionUpdateRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**subscription_pending_update** | [**UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate**](UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_update_res import UnibeeApiMerchantSubscriptionUpdateRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionUpdateRes from a JSON string
unibee_api_merchant_subscription_update_res_instance = UnibeeApiMerchantSubscriptionUpdateRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionUpdateRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_update_res_dict = unibee_api_merchant_subscription_update_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionUpdateRes from a dict
unibee_api_merchant_subscription_update_res_form_dict = unibee_api_merchant_subscription_update_res.from_dict(unibee_api_merchant_subscription_update_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


