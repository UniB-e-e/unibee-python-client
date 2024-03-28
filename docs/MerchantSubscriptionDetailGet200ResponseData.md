# MerchantSubscriptionDetailGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) | AddonParams | [optional] 
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Plan Addon | [optional] 
**gateway** | [**UnibeeApiBeanGatewaySimplify**](UnibeeApiBeanGatewaySimplify.md) |  | [optional] 
**latest_invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeApiBeanSubscriptionSimplify**](UnibeeApiBeanSubscriptionSimplify.md) |  | [optional] 
**unfinished_subscription_pending_update** | [**UnibeeApiBeanDetailSubscriptionPendingUpdateDetail**](UnibeeApiBeanDetailSubscriptionPendingUpdateDetail.md) |  | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_detail_get200_response_data import MerchantSubscriptionDetailGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionDetailGet200ResponseData from a JSON string
merchant_subscription_detail_get200_response_data_instance = MerchantSubscriptionDetailGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionDetailGet200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_detail_get200_response_data_dict = merchant_subscription_detail_get200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionDetailGet200ResponseData from a dict
merchant_subscription_detail_get200_response_data_form_dict = merchant_subscription_detail_get200_response_data.from_dict(merchant_subscription_detail_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


