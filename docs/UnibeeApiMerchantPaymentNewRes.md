# UnibeeApiMerchantPaymentNewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** |  | [optional] 
**external_payment_id** | **str** | ExternalPaymentId | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**status** | **int** | Status, 10-Created|20-Success|30-Failed|40-Cancelled | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_new_res import UnibeeApiMerchantPaymentNewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentNewRes from a JSON string
unibee_api_merchant_payment_new_res_instance = UnibeeApiMerchantPaymentNewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentNewRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_new_res_dict = unibee_api_merchant_payment_new_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentNewRes from a dict
unibee_api_merchant_payment_new_res_form_dict = unibee_api_merchant_payment_new_res.from_dict(unibee_api_merchant_payment_new_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


