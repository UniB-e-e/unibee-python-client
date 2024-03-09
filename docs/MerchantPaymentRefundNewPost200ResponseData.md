# MerchantPaymentRefundNewPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_refund_id** | **str** | ExternalRefundId | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**refund_id** | **str** | RefundId | [optional] 
**status** | **int** | Status,10-create|20-success|30-Failed|40-Reverse | [optional] 

## Example

```python
from openapi_client.models.merchant_payment_refund_new_post200_response_data import MerchantPaymentRefundNewPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaymentRefundNewPost200ResponseData from a JSON string
merchant_payment_refund_new_post200_response_data_instance = MerchantPaymentRefundNewPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantPaymentRefundNewPost200ResponseData.to_json()

# convert the object into a dict
merchant_payment_refund_new_post200_response_data_dict = merchant_payment_refund_new_post200_response_data_instance.to_dict()
# create an instance of MerchantPaymentRefundNewPost200ResponseData from a dict
merchant_payment_refund_new_post200_response_data_form_dict = merchant_payment_refund_new_post200_response_data.from_dict(merchant_payment_refund_new_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


