# MerchantPaymentNewPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** |  | [optional] 
**external_payment_id** | **str** | ExternalPaymentId | [optional] 
**link** | **str** |  | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**status** | **int** | Status, 10-Created|20-Success|30-Failed|40-Cancelled | [optional] 

## Example

```python
from openapi_client.models.merchant_payment_new_post200_response_data import MerchantPaymentNewPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPaymentNewPost200ResponseData from a JSON string
merchant_payment_new_post200_response_data_instance = MerchantPaymentNewPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantPaymentNewPost200ResponseData.to_json()

# convert the object into a dict
merchant_payment_new_post200_response_data_dict = merchant_payment_new_post200_response_data_instance.to_dict()
# create an instance of MerchantPaymentNewPost200ResponseData from a dict
merchant_payment_new_post200_response_data_form_dict = merchant_payment_new_post200_response_data.from_dict(merchant_payment_new_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


