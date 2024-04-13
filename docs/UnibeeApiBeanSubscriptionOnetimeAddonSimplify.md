# UnibeeApiBeanSubscriptionOnetimeAddonSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_id** | **int** | onetime addonId | [optional] 
**create_time** | **int** | create utc time | [optional] 
**id** | **int** | id | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**payment_link** | **str** | PaymentLink | [optional] 
**quantity** | **int** | quantity | [optional] 
**status** | **int** | status, 1-create, 2-paid, 3-cancel, 4-expired | [optional] 
**subscription_id** | **str** | subscription_id | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_subscription_onetime_addon_simplify import UnibeeApiBeanSubscriptionOnetimeAddonSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanSubscriptionOnetimeAddonSimplify from a JSON string
unibee_api_bean_subscription_onetime_addon_simplify_instance = UnibeeApiBeanSubscriptionOnetimeAddonSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanSubscriptionOnetimeAddonSimplify.to_json()

# convert the object into a dict
unibee_api_bean_subscription_onetime_addon_simplify_dict = unibee_api_bean_subscription_onetime_addon_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanSubscriptionOnetimeAddonSimplify from a dict
unibee_api_bean_subscription_onetime_addon_simplify_form_dict = unibee_api_bean_subscription_onetime_addon_simplify.from_dict(unibee_api_bean_subscription_onetime_addon_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


