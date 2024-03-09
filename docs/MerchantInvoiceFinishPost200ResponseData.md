# MerchantInvoiceFinishPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**UnibeeInternalModelEntityOverseaPayInvoice**](UnibeeInternalModelEntityOverseaPayInvoice.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_invoice_finish_post200_response_data import MerchantInvoiceFinishPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantInvoiceFinishPost200ResponseData from a JSON string
merchant_invoice_finish_post200_response_data_instance = MerchantInvoiceFinishPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantInvoiceFinishPost200ResponseData.to_json()

# convert the object into a dict
merchant_invoice_finish_post200_response_data_dict = merchant_invoice_finish_post200_response_data_instance.to_dict()
# create an instance of MerchantInvoiceFinishPost200ResponseData from a dict
merchant_invoice_finish_post200_response_data_form_dict = merchant_invoice_finish_post200_response_data.from_dict(merchant_invoice_finish_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


