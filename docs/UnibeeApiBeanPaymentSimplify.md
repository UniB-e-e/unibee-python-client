# UnibeeApiBeanPaymentSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_reason** | **str** |  | [optional] 
**authorize_status** | **int** | authorize status，0-waiting authorize，1-authorized，2-authorized_request | [optional] 
**automatic** | **int** |  | [optional] 
**balance_amount** | **int** | balance_amount | [optional] 
**billing_reason** | **str** |  | [optional] 
**cancel_time** | **int** | cancel time, utc time | [optional] 
**country_code** | **str** | country code | [optional] 
**create_time** | **int** | create time, utc time | [optional] 
**currency** | **str** | currency，“SGD” “MYR” “PHP” “IDR” “THB” | [optional] 
**external_payment_id** | **str** | external_payment_id | [optional] 
**failure_reason** | **str** |  | [optional] 
**gas_payer** | **str** | who pay the gas, merchant|user | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_payment_id** | **str** | gateway_payment_id | [optional] 
**invoice_id** | **str** | invoice id | [optional] 
**link** | **str** |  | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**paid_time** | **int** | paid time, utc time | [optional] 
**payment_amount** | **int** | payment_amount | [optional] 
**payment_id** | **str** | payment id | [optional] 
**refund_amount** | **int** | total refund amount | [optional] 
**return_url** | **str** | return url | [optional] 
**status** | **int** | status  10-pending，20-success，30-failure, 40-cancel | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**total_amount** | **int** | total amount | [optional] 
**user_id** | **int** | user_id | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_payment_simplify import UnibeeApiBeanPaymentSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPaymentSimplify from a JSON string
unibee_api_bean_payment_simplify_instance = UnibeeApiBeanPaymentSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPaymentSimplify.to_json()

# convert the object into a dict
unibee_api_bean_payment_simplify_dict = unibee_api_bean_payment_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanPaymentSimplify from a dict
unibee_api_bean_payment_simplify_form_dict = unibee_api_bean_payment_simplify.from_dict(unibee_api_bean_payment_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


