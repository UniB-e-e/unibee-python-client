# UnibeeApiMerchantInvoiceFinishReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_util_due** | **int** | DaysUtilDue,Due Day Of Pay | 
**invoice_id** | **str** | InvoiceId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_finish_req import UnibeeApiMerchantInvoiceFinishReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceFinishReq from a JSON string
unibee_api_merchant_invoice_finish_req_instance = UnibeeApiMerchantInvoiceFinishReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceFinishReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_finish_req_dict = unibee_api_merchant_invoice_finish_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceFinishReq from a dict
unibee_api_merchant_invoice_finish_req_form_dict = unibee_api_merchant_invoice_finish_req.from_dict(unibee_api_merchant_invoice_finish_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


