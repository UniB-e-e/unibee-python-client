# UnibeeInternalModelEntityOverseaPayPaymentTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**gateway_id** | **int** | gateway id | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**id** | **int** |  | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**status** | **int** | 0-pending, 1-success, 2-failure | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**timeline_type** | **int** | 0-pay, 1-refund | [optional] 
**total_amount** | **int** | total amount | [optional] 
**unique_id** | **str** | unique id | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_payment_timeline import UnibeeInternalModelEntityOverseaPayPaymentTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayPaymentTimeline from a JSON string
unibee_internal_model_entity_oversea_pay_payment_timeline_instance = UnibeeInternalModelEntityOverseaPayPaymentTimeline.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayPaymentTimeline.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_payment_timeline_dict = unibee_internal_model_entity_oversea_pay_payment_timeline_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayPaymentTimeline from a dict
unibee_internal_model_entity_oversea_pay_payment_timeline_form_dict = unibee_internal_model_entity_oversea_pay_payment_timeline.from_dict(unibee_internal_model_entity_oversea_pay_payment_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


