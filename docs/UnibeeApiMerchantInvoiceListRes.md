# UnibeeApiMerchantInvoiceListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | [**List[UnibeeApiBeanDetailInvoiceDetail]**](UnibeeApiBeanDetailInvoiceDetail.md) | invoice Detail List | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_list_res import UnibeeApiMerchantInvoiceListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceListRes from a JSON string
unibee_api_merchant_invoice_list_res_instance = UnibeeApiMerchantInvoiceListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceListRes.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_list_res_dict = unibee_api_merchant_invoice_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceListRes from a dict
unibee_api_merchant_invoice_list_res_form_dict = unibee_api_merchant_invoice_list_res.from_dict(unibee_api_merchant_invoice_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


