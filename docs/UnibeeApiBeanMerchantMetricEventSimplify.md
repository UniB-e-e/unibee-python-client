# UnibeeApiBeanMerchantMetricEventSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_property_data** | **str** | aggregation property data (Json) | [optional] 
**aggregation_property_int** | **int** | aggregation property int, use for metric of max|sum type | [optional] 
**aggregation_property_string** | **str** | aggregation property string, use for metric of count|count_unique type | [optional] 
**create_time** | **int** | create utc time | [optional] 
**external_event_id** | **str** | external_event_id, should be unique | [optional] 
**id** | **int** | Id | [optional] 
**merchant_id** | **int** | merchantId | [optional] 
**metric_id** | **int** | metric_id | [optional] 
**metric_limit** | **int** |  | [optional] 
**subscription_ids** | **str** |  | [optional] 
**subscription_period_end** | **int** | matched subscription&#39;s current_period_end | [optional] 
**subscription_period_start** | **int** | matched subscription&#39;s current_period_start | [optional] 
**used** | **int** |  | [optional] 
**user_id** | **int** | user_id | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_metric_event_simplify import UnibeeApiBeanMerchantMetricEventSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantMetricEventSimplify from a JSON string
unibee_api_bean_merchant_metric_event_simplify_instance = UnibeeApiBeanMerchantMetricEventSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantMetricEventSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_metric_event_simplify_dict = unibee_api_bean_merchant_metric_event_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantMetricEventSimplify from a dict
unibee_api_bean_merchant_metric_event_simplify_form_dict = unibee_api_bean_merchant_metric_event_simplify.from_dict(unibee_api_bean_merchant_metric_event_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


