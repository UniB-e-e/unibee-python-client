# UnibeeApiMerchantPaymentCancelReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | PaymentId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_cancel_req import UnibeeApiMerchantPaymentCancelReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentCancelReq from a JSON string
unibee_api_merchant_payment_cancel_req_instance = UnibeeApiMerchantPaymentCancelReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentCancelReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_cancel_req_dict = unibee_api_merchant_payment_cancel_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentCancelReq from a dict
unibee_api_merchant_payment_cancel_req_form_dict = unibee_api_merchant_payment_cancel_req.from_dict(unibee_api_merchant_payment_cancel_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


