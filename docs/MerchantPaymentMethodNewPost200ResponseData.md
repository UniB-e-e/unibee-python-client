# MerchantPaymentMethodNewPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**UnibeeApiBeanPaymentMethod**](UnibeeApiBeanPaymentMethod.md) |  | [optional] 
**url** | **str** | Url | [optional] 

## Example

```python
from openapi_client.models.merchant_payment_method_new_post200_response_data import MerchantPaymentMethodNewPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaymentMethodNewPost200ResponseData from a JSON string
merchant_payment_method_new_post200_response_data_instance = MerchantPaymentMethodNewPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantPaymentMethodNewPost200ResponseData.to_json()

# convert the object into a dict
merchant_payment_method_new_post200_response_data_dict = merchant_payment_method_new_post200_response_data_instance.to_dict()
# create an instance of MerchantPaymentMethodNewPost200ResponseData from a dict
merchant_payment_method_new_post200_response_data_form_dict = merchant_payment_method_new_post200_response_data.from_dict(merchant_payment_method_new_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


