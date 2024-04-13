# UnibeeApiMerchantPaymentMethodNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**data** | **object** |  | [optional] 
**gateway_id** | **int** | GatewayId | 
**redirect_url** | **str** | Redirect Url | [optional] 
**subscription_id** | **str** | if provide, bind to it | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** | UserId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_method_new_req import UnibeeApiMerchantPaymentMethodNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentMethodNewReq from a JSON string
unibee_api_merchant_payment_method_new_req_instance = UnibeeApiMerchantPaymentMethodNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentMethodNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_method_new_req_dict = unibee_api_merchant_payment_method_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentMethodNewReq from a dict
unibee_api_merchant_payment_method_new_req_form_dict = unibee_api_merchant_payment_method_new_req.from_dict(unibee_api_merchant_payment_method_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


