# UnibeeApiMerchantPaymentCaptureReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_amount** | **int** | CaptureAmount, Cent | 
**currency** | **str** | Currency | 
**external_capture_id** | **str** | ExternalCaptureId | 
**payment_id** | **str** | PaymentId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_capture_req import UnibeeApiMerchantPaymentCaptureReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentCaptureReq from a JSON string
unibee_api_merchant_payment_capture_req_instance = UnibeeApiMerchantPaymentCaptureReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentCaptureReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_capture_req_dict = unibee_api_merchant_payment_capture_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentCaptureReq from a dict
unibee_api_merchant_payment_capture_req_form_dict = unibee_api_merchant_payment_capture_req.from_dict(unibee_api_merchant_payment_capture_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


