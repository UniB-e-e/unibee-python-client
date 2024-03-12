# UnibeeApiBeanMerchantMetricSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_property** | **str** | aggregation property | [optional] 
**aggregation_type** | **int** | 1-count，2-count unique, 3-latest, 4-max, 5-sum | [optional] 
**code** | **str** | code | [optional] 
**create_time** | **int** | create utc time | [optional] 
**gmt_modify** | **int** | update time | [optional] 
**id** | **int** | id | [optional] 
**merchant_id** | **int** | merchantId | [optional] 
**metric_description** | **str** | metric description | [optional] 
**metric_name** | **str** | metric name | [optional] 
**type** | **int** | 1-limit_metered，2-charge_metered(come later),3-charge_recurring(come later) | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_metric_simplify import UnibeeApiBeanMerchantMetricSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantMetricSimplify from a JSON string
unibee_api_bean_merchant_metric_simplify_instance = UnibeeApiBeanMerchantMetricSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantMetricSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_metric_simplify_dict = unibee_api_bean_merchant_metric_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantMetricSimplify from a dict
unibee_api_bean_merchant_metric_simplify_form_dict = unibee_api_bean_merchant_metric_simplify.from_dict(unibee_api_bean_merchant_metric_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


