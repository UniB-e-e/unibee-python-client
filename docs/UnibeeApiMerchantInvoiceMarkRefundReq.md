# UnibeeApiMerchantInvoiceMarkRefundReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | InvoiceId | 
**reason** | **str** | Refund Reason | 
**refund_amount** | **int** | Refund CaptureAmount | 
**refund_no** | **str** | RefundNo | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_mark_refund_req import UnibeeApiMerchantInvoiceMarkRefundReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceMarkRefundReq from a JSON string
unibee_api_merchant_invoice_mark_refund_req_instance = UnibeeApiMerchantInvoiceMarkRefundReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceMarkRefundReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_mark_refund_req_dict = unibee_api_merchant_invoice_mark_refund_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceMarkRefundReq from a dict
unibee_api_merchant_invoice_mark_refund_req_form_dict = unibee_api_merchant_invoice_mark_refund_req.from_dict(unibee_api_merchant_invoice_mark_refund_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


