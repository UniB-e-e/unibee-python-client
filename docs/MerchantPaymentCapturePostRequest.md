# MerchantPaymentCapturePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_capture_id** | **str** | ExternalCaptureId | 
**payment_id** | **str** | PaymentId | 

## Example

```python
from openapi_client.models.merchant_payment_capture_post_request import MerchantPaymentCapturePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaymentCapturePostRequest from a JSON string
merchant_payment_capture_post_request_instance = MerchantPaymentCapturePostRequest.from_json(json)
# print the JSON string representation of the object
print MerchantPaymentCapturePostRequest.to_json()

# convert the object into a dict
merchant_payment_capture_post_request_dict = merchant_payment_capture_post_request_instance.to_dict()
# create an instance of MerchantPaymentCapturePostRequest from a dict
merchant_payment_capture_post_request_form_dict = merchant_payment_capture_post_request.from_dict(merchant_payment_capture_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


