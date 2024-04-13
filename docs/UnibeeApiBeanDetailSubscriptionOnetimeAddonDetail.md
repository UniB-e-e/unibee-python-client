# UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**addon_id** | **int** | onetime addonId | [optional] 
**create_time** | **int** | create utc time | [optional] 
**id** | **int** | id | [optional] 
**metadata** | **Dict[str, str]** | Metadata | [optional] 
**payment** | [**UnibeeApiBeanPaymentSimplify**](UnibeeApiBeanPaymentSimplify.md) |  | [optional] 
**quantity** | **int** | quantity | [optional] 
**status** | **int** | status, 1-create, 2-paid, 3-cancel, 4-expired | [optional] 
**subscription_id** | **str** | subscription_id | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_detail_subscription_onetime_addon_detail import UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail from a JSON string
unibee_api_bean_detail_subscription_onetime_addon_detail_instance = UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail.to_json()

# convert the object into a dict
unibee_api_bean_detail_subscription_onetime_addon_detail_dict = unibee_api_bean_detail_subscription_onetime_addon_detail_instance.to_dict()
# create an instance of UnibeeApiBeanDetailSubscriptionOnetimeAddonDetail from a dict
unibee_api_bean_detail_subscription_onetime_addon_detail_form_dict = unibee_api_bean_detail_subscription_onetime_addon_detail.from_dict(unibee_api_bean_detail_subscription_onetime_addon_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


