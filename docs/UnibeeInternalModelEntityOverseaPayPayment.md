# UnibeeInternalModelEntityOverseaPayPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **str** | addtional data (json) | [optional] 
**app_id** | **str** | app id | [optional] 
**authorize_reason** | **str** |  | [optional] 
**authorize_status** | **int** | authorize status，0-waiting authorize，1-authorized，2-authorized_request | [optional] 
**automatic** | **int** |  | [optional] 
**balance_amount** | **int** | balance_amount | [optional] 
**balance_end** | **int** | balance_end, utc time | [optional] 
**balance_start** | **int** | balance_start, utc time | [optional] 
**billing_reason** | **str** |  | [optional] 
**biz_type** | **int** | biz_type 1-single payment, 3-subscription | [optional] 
**cancel_time** | **int** | cancel time, utc time | [optional] 
**capture_delay_hours** | **int** | capture_delay_hours | [optional] 
**code** | **str** |  | [optional] 
**company_id** | **int** | company id | [optional] 
**country_code** | **str** | country code | [optional] 
**create_time** | **int** | create time, utc time | [optional] 
**currency** | **str** | currency，“SGD” “MYR” “PHP” “IDR” “THB” | [optional] 
**external_payment_id** | **str** | external_payment_id | [optional] 
**failure_reason** | **str** |  | [optional] 
**gateway_edition** | **str** | gateway edition | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_payment_id** | **str** | gateway_payment_id | [optional] 
**gateway_payment_intent_id** | **str** | gateway_payment_intent_id | [optional] 
**gateway_payment_method** | **str** |  | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**hide_payment_methods** | **str** | hide_payment_methods | [optional] 
**id** | **int** | id | [optional] 
**invoice_data** | **str** |  | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**link** | **str** |  | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**open_api_id** | **int** | open api id | [optional] 
**paid_time** | **int** | paid time, utc time | [optional] 
**payment_amount** | **int** | payment_amount | [optional] 
**payment_data** | **str** | payment create data (json) | [optional] 
**payment_id** | **str** | payment id | [optional] 
**refund_amount** | **int** | total refund amount | [optional] 
**return_url** | **str** | return url | [optional] 
**status** | **int** | status  10-pending，20-success，30-failure, 40-cancel | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**terminal_ip** | **str** | client ip | [optional] 
**token** | **str** |  | [optional] 
**total_amount** | **int** | total amount | [optional] 
**unique_id** | **str** | unique id | [optional] 
**user_id** | **int** | user_id | [optional] 
**verify** | **str** | codeVerify | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_payment import UnibeeInternalModelEntityOverseaPayPayment

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayPayment from a JSON string
unibee_internal_model_entity_oversea_pay_payment_instance = UnibeeInternalModelEntityOverseaPayPayment.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayPayment.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_payment_dict = unibee_internal_model_entity_oversea_pay_payment_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayPayment from a dict
unibee_internal_model_entity_oversea_pay_payment_form_dict = unibee_internal_model_entity_oversea_pay_payment.from_dict(unibee_internal_model_entity_oversea_pay_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


