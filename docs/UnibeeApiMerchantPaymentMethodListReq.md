# UnibeeApiMerchantPaymentMethodListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **int** | GatewayId | 
**payment_id** | **str** | PaymentId | [optional] 
**user_id** | **int** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_method_list_req import UnibeeApiMerchantPaymentMethodListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentMethodListReq from a JSON string
unibee_api_merchant_payment_method_list_req_instance = UnibeeApiMerchantPaymentMethodListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentMethodListReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_method_list_req_dict = unibee_api_merchant_payment_method_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentMethodListReq from a dict
unibee_api_merchant_payment_method_list_req_form_dict = unibee_api_merchant_payment_method_list_req.from_dict(unibee_api_merchant_payment_method_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


