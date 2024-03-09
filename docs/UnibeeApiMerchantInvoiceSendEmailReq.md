# UnibeeApiMerchantInvoiceSendEmailReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID | 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_send_email_req import UnibeeApiMerchantInvoiceSendEmailReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceSendEmailReq from a JSON string
unibee_api_merchant_invoice_send_email_req_instance = UnibeeApiMerchantInvoiceSendEmailReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceSendEmailReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_send_email_req_dict = unibee_api_merchant_invoice_send_email_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceSendEmailReq from a dict
unibee_api_merchant_invoice_send_email_req_form_dict = unibee_api_merchant_invoice_send_email_req.from_dict(unibee_api_merchant_invoice_send_email_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


