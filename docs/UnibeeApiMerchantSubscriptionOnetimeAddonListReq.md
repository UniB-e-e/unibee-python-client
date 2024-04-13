# UnibeeApiMerchantSubscriptionOnetimeAddonListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**page** | **int** | Page, Start With 0 | [optional] 
**user_id** | **int** | UserId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_onetime_addon_list_req import UnibeeApiMerchantSubscriptionOnetimeAddonListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonListReq from a JSON string
unibee_api_merchant_subscription_onetime_addon_list_req_instance = UnibeeApiMerchantSubscriptionOnetimeAddonListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionOnetimeAddonListReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_onetime_addon_list_req_dict = unibee_api_merchant_subscription_onetime_addon_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionOnetimeAddonListReq from a dict
unibee_api_merchant_subscription_onetime_addon_list_req_form_dict = unibee_api_merchant_subscription_onetime_addon_list_req.from_dict(unibee_api_merchant_subscription_onetime_addon_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


