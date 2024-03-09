# UnibeeApiMerchantInvoiceNewInvoiceItemParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_amount_excluding_tax** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_new_invoice_item_param import UnibeeApiMerchantInvoiceNewInvoiceItemParam

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceNewInvoiceItemParam from a JSON string
unibee_api_merchant_invoice_new_invoice_item_param_instance = UnibeeApiMerchantInvoiceNewInvoiceItemParam.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceNewInvoiceItemParam.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_new_invoice_item_param_dict = unibee_api_merchant_invoice_new_invoice_item_param_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceNewInvoiceItemParam from a dict
unibee_api_merchant_invoice_new_invoice_item_param_form_dict = unibee_api_merchant_invoice_new_invoice_item_param.from_dict(unibee_api_merchant_invoice_new_invoice_item_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


