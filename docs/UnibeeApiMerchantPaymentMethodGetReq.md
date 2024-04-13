# UnibeeApiMerchantPaymentMethodGetReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **int** | GatewayId | 
**payment_method_id** | **str** | PaymentMethodId | 
**user_id** | **int** | UserId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_method_get_req import UnibeeApiMerchantPaymentMethodGetReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentMethodGetReq from a JSON string
unibee_api_merchant_payment_method_get_req_instance = UnibeeApiMerchantPaymentMethodGetReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentMethodGetReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_method_get_req_dict = unibee_api_merchant_payment_method_get_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentMethodGetReq from a dict
unibee_api_merchant_payment_method_get_req_form_dict = unibee_api_merchant_payment_method_get_req.from_dict(unibee_api_merchant_payment_method_get_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


