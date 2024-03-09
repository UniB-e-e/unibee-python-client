# UnibeeApiMerchantInvoicePdfGenerateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID | 
**send_user_email** | **bool** | Whether Send Invoice Email To User Or Not，Default Not Send | [optional] [default to False]

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_pdf_generate_req import UnibeeApiMerchantInvoicePdfGenerateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoicePdfGenerateReq from a JSON string
unibee_api_merchant_invoice_pdf_generate_req_instance = UnibeeApiMerchantInvoicePdfGenerateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoicePdfGenerateReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_pdf_generate_req_dict = unibee_api_merchant_invoice_pdf_generate_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoicePdfGenerateReq from a dict
unibee_api_merchant_invoice_pdf_generate_req_form_dict = unibee_api_merchant_invoice_pdf_generate_req.from_dict(unibee_api_merchant_invoice_pdf_generate_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


