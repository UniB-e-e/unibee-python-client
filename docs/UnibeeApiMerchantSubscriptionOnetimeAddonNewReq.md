# UnibeeApiMerchantSubscriptionOnetimeAddonNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_id** | **int** | AddonId, id of one-time addon, the new payment will created base on the addon&#39;s amount&#39; | 
**discount_code** | **str** | DiscountCode | [optional] 
**metadata** | **Dict[str, str]** | Metadata，custom data | [optional] 
**quantity** | **int** | Quantity, quantity of the new payment which one-time addon purchased | 
**return_url** | **str** | ReturnUrl, the addon&#39;s payment will redirect based on the returnUrl provided when it&#39;s back from gateway side | [optional] 
**subscription_id** | **str** | SubscriptionId, id of subscription which addon will attached | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_onetime_addon_new_req import UnibeeApiMerchantSubscriptionOnetimeAddonNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewReq from a JSON string
unibee_api_merchant_subscription_onetime_addon_new_req_instance = UnibeeApiMerchantSubscriptionOnetimeAddonNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionOnetimeAddonNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_onetime_addon_new_req_dict = unibee_api_merchant_subscription_onetime_addon_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonNewReq from a dict
unibee_api_merchant_subscription_onetime_addon_new_req_form_dict = unibee_api_merchant_subscription_onetime_addon_new_req.from_dict(unibee_api_merchant_subscription_onetime_addon_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


