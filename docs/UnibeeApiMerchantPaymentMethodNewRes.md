# UnibeeApiMerchantPaymentMethodNewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**UnibeeApiBeanPaymentMethod**](UnibeeApiBeanPaymentMethod.md) |  | [optional] 
**url** | **str** | Url | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_method_new_res import UnibeeApiMerchantPaymentMethodNewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentMethodNewRes from a JSON string
unibee_api_merchant_payment_method_new_res_instance = UnibeeApiMerchantPaymentMethodNewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentMethodNewRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_method_new_res_dict = unibee_api_merchant_payment_method_new_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentMethodNewRes from a dict
unibee_api_merchant_payment_method_new_res_form_dict = unibee_api_merchant_payment_method_new_res.from_dict(unibee_api_merchant_payment_method_new_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


