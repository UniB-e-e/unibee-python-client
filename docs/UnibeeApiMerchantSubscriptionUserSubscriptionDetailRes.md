# UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Plan Addon | [optional] 
**gateway** | [**UnibeeApiBeanGatewaySimplify**](UnibeeApiBeanGatewaySimplify.md) |  | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeApiBeanSubscriptionSimplify**](UnibeeApiBeanSubscriptionSimplify.md) |  | [optional] 
**unfinished_subscription_pending_update** | [**UnibeeApiBeanSubscriptionPendingUpdateDetail**](UnibeeApiBeanSubscriptionPendingUpdateDetail.md) |  | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_user_subscription_detail_res import UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes from a JSON string
unibee_api_merchant_subscription_user_subscription_detail_res_instance = UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_user_subscription_detail_res_dict = unibee_api_merchant_subscription_user_subscription_detail_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionUserSubscriptionDetailRes from a dict
unibee_api_merchant_subscription_user_subscription_detail_res_form_dict = unibee_api_merchant_subscription_user_subscription_detail_res.from_dict(unibee_api_merchant_subscription_user_subscription_detail_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


