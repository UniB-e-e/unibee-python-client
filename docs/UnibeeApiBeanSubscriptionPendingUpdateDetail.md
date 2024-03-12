# UnibeeApiBeanSubscriptionPendingUpdateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_data** | **str** | plan addon json data | [optional] 
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Addons | [optional] 
**amount** | **int** | CaptureAmount, Cent | [optional] 
**currency** | **str** | Currency | [optional] 
**effect_immediate** | **int** | EffectImmediate | [optional] 
**effect_time** | **int** | effect_immediate&#x3D;0, EffectTime unit_time | [optional] 
**gateway_id** | **int** | Id | [optional] 
**gmt_create** | **str** | GmtCreate | [optional] 
**gmt_modify** | **str** | GmtModify | [optional] 
**link** | **str** | Link | [optional] 
**merchant_id** | **int** | MerchantId | [optional] 
**merchant_member** | [**UnibeeApiBeanMerchantMemberSimplify**](UnibeeApiBeanMerchantMemberSimplify.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**note** | **str** | Update Note | [optional] 
**paid** | **int** | Paid | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**plan_id** | **int** | PlanId | [optional] 
**proration_amount** | **int** | ProrationAmount,Cents | [optional] 
**quantity** | **int** | quantity | [optional] 
**status** | **int** | Status，0-Init | 1-Create｜2-Finished｜3-Cancelled | [optional] 
**subscription_id** | **str** | SubscriptionId | [optional] 
**update_addon_data** | **str** | UpdateAddonData | [optional] 
**update_addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | UpdateAddons | [optional] 
**update_amount** | **int** | UpdateAmount, Cents | [optional] 
**update_currency** | **str** | UpdateCurrency | [optional] 
**update_plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**update_plan_id** | **int** | UpdatePlanId | [optional] 
**update_quantity** | **int** | UpdateQuantity | [optional] 
**update_subscription_id** | **str** | UpdateSubscriptionId | [optional] 
**user_id** | **int** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_subscription_pending_update_detail import UnibeeApiBeanSubscriptionPendingUpdateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanSubscriptionPendingUpdateDetail from a JSON string
unibee_api_bean_subscription_pending_update_detail_instance = UnibeeApiBeanSubscriptionPendingUpdateDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanSubscriptionPendingUpdateDetail.to_json()

# convert the object into a dict
unibee_api_bean_subscription_pending_update_detail_dict = unibee_api_bean_subscription_pending_update_detail_instance.to_dict()
# create an instance of UnibeeApiBeanSubscriptionPendingUpdateDetail from a dict
unibee_api_bean_subscription_pending_update_detail_form_dict = unibee_api_bean_subscription_pending_update_detail.from_dict(unibee_api_bean_subscription_pending_update_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


