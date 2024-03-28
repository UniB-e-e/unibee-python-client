# UnibeeApiMerchantSubscriptionRenewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | SubscriptionId | 
**user_id** | **int** | UserId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_renew_req import UnibeeApiMerchantSubscriptionRenewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionRenewReq from a JSON string
unibee_api_merchant_subscription_renew_req_instance = UnibeeApiMerchantSubscriptionRenewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionRenewReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_renew_req_dict = unibee_api_merchant_subscription_renew_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionRenewReq from a dict
unibee_api_merchant_subscription_renew_req_form_dict = unibee_api_merchant_subscription_renew_req.from_dict(unibee_api_merchant_subscription_renew_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


