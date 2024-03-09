# UnibeeApiMerchantInvoiceListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_end** | **int** | AmountEnd | [optional] 
**amount_start** | **int** | AmountStart | [optional] 
**count** | **int** | Count By Page | [optional] 
**currency** | **str** | Currency | [optional] 
**delete_include** | **bool** | Deleted Involved，Need Admin | [optional] 
**first_name** | **str** | FirstName | [optional] 
**last_name** | **str** | LastName | [optional] 
**page** | **int** | Page, Start 0 | [optional] 
**send_email** | **str** | SendEmail Filter , Default Filter All | [optional] 
**sort_field** | **str** | Filter，em. invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify | [optional] 
**sort_type** | **str** | Sort，asc|desc，Default desc | [optional] 
**status** | **List[int]** | Status, 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled | [optional] 
**user_id** | **int** | UserId Filter, Default Filter All | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_list_req import UnibeeApiMerchantInvoiceListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceListReq from a JSON string
unibee_api_merchant_invoice_list_req_instance = UnibeeApiMerchantInvoiceListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceListReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_list_req_dict = unibee_api_merchant_invoice_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceListReq from a dict
unibee_api_merchant_invoice_list_req_form_dict = unibee_api_merchant_invoice_list_req.from_dict(unibee_api_merchant_invoice_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


