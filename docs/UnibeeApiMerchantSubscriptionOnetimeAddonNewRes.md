# UnibeeApiMerchantSubscriptionOnetimeAddonNewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**link** | **str** | if automatic payment is false, Gateway Link will provided that manual payment needed | [optional] 
**paid** | **bool** | true|false,automatic payment is default behavior for one-time addon purchased, payment will create attach to the purchase, when payment is success, return false, otherwise false | [optional] 
**subscription_onetime_addon** | [**UnibeeApiBeanSubscriptionOnetimeAddonSimplify**](UnibeeApiBeanSubscriptionOnetimeAddonSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_onetime_addon_new_res import UnibeeApiMerchantSubscriptionOnetimeAddonNewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewRes from a JSON string
unibee_api_merchant_subscription_onetime_addon_new_res_instance = UnibeeApiMerchantSubscriptionOnetimeAddonNewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionOnetimeAddonNewRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_onetime_addon_new_res_dict = unibee_api_merchant_subscription_onetime_addon_new_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewRes from a dict
unibee_api_merchant_subscription_onetime_addon_new_res_form_dict = unibee_api_merchant_subscription_onetime_addon_new_res.from_dict(unibee_api_merchant_subscription_onetime_addon_new_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


