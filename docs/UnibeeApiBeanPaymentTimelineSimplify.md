# UnibeeApiBeanPaymentTimelineSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**gateway_id** | **int** | gateway id | [optional] 
**id** | **int** |  | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**status** | **int** | 0-pending, 1-success, 2-failure | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**timeline_type** | **int** | 0-pay, 1-refund | [optional] 
**total_amount** | **int** | total amount | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_payment_timeline_simplify import UnibeeApiBeanPaymentTimelineSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPaymentTimelineSimplify from a JSON string
unibee_api_bean_payment_timeline_simplify_instance = UnibeeApiBeanPaymentTimelineSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPaymentTimelineSimplify.to_json()

# convert the object into a dict
unibee_api_bean_payment_timeline_simplify_dict = unibee_api_bean_payment_timeline_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanPaymentTimelineSimplify from a dict
unibee_api_bean_payment_timeline_simplify_form_dict = unibee_api_bean_payment_timeline_simplify.from_dict(unibee_api_bean_payment_timeline_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


