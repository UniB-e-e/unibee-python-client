# UnibeeApiMerchantSubscriptionCreateRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**subscription** | [**UnibeeApiBeanSubscriptionSimplify**](UnibeeApiBeanSubscriptionSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_create_res import UnibeeApiMerchantSubscriptionCreateRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionCreateRes from a JSON string
unibee_api_merchant_subscription_create_res_instance = UnibeeApiMerchantSubscriptionCreateRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionCreateRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_create_res_dict = unibee_api_merchant_subscription_create_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionCreateRes from a dict
unibee_api_merchant_subscription_create_res_form_dict = unibee_api_merchant_subscription_create_res.from_dict(unibee_api_merchant_subscription_create_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


