# UnibeeApiMerchantInvoiceFinishRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**UnibeeInternalModelEntityOverseaPayInvoice**](UnibeeInternalModelEntityOverseaPayInvoice.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_finish_res import UnibeeApiMerchantInvoiceFinishRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceFinishRes from a JSON string
unibee_api_merchant_invoice_finish_res_instance = UnibeeApiMerchantInvoiceFinishRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceFinishRes.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_finish_res_dict = unibee_api_merchant_invoice_finish_res_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceFinishRes from a dict
unibee_api_merchant_invoice_finish_res_form_dict = unibee_api_merchant_invoice_finish_res.from_dict(unibee_api_merchant_invoice_finish_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


