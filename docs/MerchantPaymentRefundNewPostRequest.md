# MerchantPaymentRefundNewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_refund_id** | **str** | ExternalRefundId | 
**payment_id** | **str** | PaymentId | 
**reason** | **str** | Reason | [optional] 

## Example

```python
from openapi_client.models.merchant_payment_refund_new_post_request import MerchantPaymentRefundNewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaymentRefundNewPostRequest from a JSON string
merchant_payment_refund_new_post_request_instance = MerchantPaymentRefundNewPostRequest.from_json(json)
# print the JSON string representation of the object
print MerchantPaymentRefundNewPostRequest.to_json()

# convert the object into a dict
merchant_payment_refund_new_post_request_dict = merchant_payment_refund_new_post_request_instance.to_dict()
# create an instance of MerchantPaymentRefundNewPostRequest from a dict
merchant_payment_refund_new_post_request_form_dict = merchant_payment_refund_new_post_request.from_dict(merchant_payment_refund_new_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


