# UnibeeApiBeanSubscriptionTimeLineDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Addon | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**period_end** | **int** | period_end | [optional] 
**period_end_time** | **str** | period end (datatime) | [optional] 
**period_start** | **int** | period_start | [optional] 
**period_start_time** | **str** | period start (datetime) | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**plan_id** | **int** | PlanId | [optional] 
**quantity** | **int** | quantity | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**unique_id** | **str** | unique id | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_subscription_time_line_detail import UnibeeApiBeanSubscriptionTimeLineDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanSubscriptionTimeLineDetail from a JSON string
unibee_api_bean_subscription_time_line_detail_instance = UnibeeApiBeanSubscriptionTimeLineDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanSubscriptionTimeLineDetail.to_json()

# convert the object into a dict
unibee_api_bean_subscription_time_line_detail_dict = unibee_api_bean_subscription_time_line_detail_instance.to_dict()
# create an instance of UnibeeApiBeanSubscriptionTimeLineDetail from a dict
unibee_api_bean_subscription_time_line_detail_form_dict = unibee_api_bean_subscription_time_line_detail.from_dict(unibee_api_bean_subscription_time_line_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


