# MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**link** | **str** | if automatic payment is false, Gateway Link will provided that manual payment needed | [optional] 
**paid** | **bool** | true|false,automatic payment is default behavior for one-time addon purchased, payment will create attach to the purchase, when payment is success, return false, otherwise false | [optional] 
**subscription_onetime_addon** | [**UnibeeApiBeanSubscriptionOnetimeAddonSimplify**](UnibeeApiBeanSubscriptionOnetimeAddonSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_new_onetime_addon_payment_post200_response_data import MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData from a JSON string
merchant_subscription_new_onetime_addon_payment_post200_response_data_instance = MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_new_onetime_addon_payment_post200_response_data_dict = merchant_subscription_new_onetime_addon_payment_post200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData from a dict
merchant_subscription_new_onetime_addon_payment_post200_response_data_form_dict = merchant_subscription_new_onetime_addon_payment_post200_response_data.from_dict(merchant_subscription_new_onetime_addon_payment_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


