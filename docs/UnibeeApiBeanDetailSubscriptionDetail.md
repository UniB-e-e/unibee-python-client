# UnibeeApiBeanDetailSubscriptionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) | AddonParams | [optional] 
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Addon | [optional] 
**gateway** | [**UnibeeApiBeanGatewaySimplify**](UnibeeApiBeanGatewaySimplify.md) |  | [optional] 
**latest_invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeApiBeanSubscriptionSimplify**](UnibeeApiBeanSubscriptionSimplify.md) |  | [optional] 
**unfinished_subscription_pending_update** | [**UnibeeApiBeanDetailSubscriptionPendingUpdateDetail**](UnibeeApiBeanDetailSubscriptionPendingUpdateDetail.md) |  | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_detail_subscription_detail import UnibeeApiBeanDetailSubscriptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanDetailSubscriptionDetail from a JSON string
unibee_api_bean_detail_subscription_detail_instance = UnibeeApiBeanDetailSubscriptionDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanDetailSubscriptionDetail.to_json()

# convert the object into a dict
unibee_api_bean_detail_subscription_detail_dict = unibee_api_bean_detail_subscription_detail_instance.to_dict()
# create an instance of UnibeeApiBeanDetailSubscriptionDetail from a dict
unibee_api_bean_detail_subscription_detail_form_dict = unibee_api_bean_detail_subscription_detail.from_dict(unibee_api_bean_detail_subscription_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


