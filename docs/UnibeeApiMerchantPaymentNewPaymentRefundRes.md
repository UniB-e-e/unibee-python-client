# UnibeeApiMerchantPaymentNewPaymentRefundRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_refund_id** | **str** | ExternalRefundId | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**refund_id** | **str** | RefundId | [optional] 
**status** | **int** | Status,10-create|20-success|30-Failed|40-Reverse | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_new_payment_refund_res import UnibeeApiMerchantPaymentNewPaymentRefundRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentNewPaymentRefundRes from a JSON string
unibee_api_merchant_payment_new_payment_refund_res_instance = UnibeeApiMerchantPaymentNewPaymentRefundRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentNewPaymentRefundRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_new_payment_refund_res_dict = unibee_api_merchant_payment_new_payment_refund_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentNewPaymentRefundRes from a dict
unibee_api_merchant_payment_new_payment_refund_res_form_dict = unibee_api_merchant_payment_new_payment_refund_res.from_dict(unibee_api_merchant_payment_new_payment_refund_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


