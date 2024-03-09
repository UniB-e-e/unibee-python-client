# UnibeeApiMerchantInvoiceEditRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**UnibeeInternalLogicGatewayRoInvoiceDetailRo**](UnibeeInternalLogicGatewayRoInvoiceDetailRo.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_edit_res import UnibeeApiMerchantInvoiceEditRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceEditRes from a JSON string
unibee_api_merchant_invoice_edit_res_instance = UnibeeApiMerchantInvoiceEditRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceEditRes.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_edit_res_dict = unibee_api_merchant_invoice_edit_res_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceEditRes from a dict
unibee_api_merchant_invoice_edit_res_form_dict = unibee_api_merchant_invoice_edit_res.from_dict(unibee_api_merchant_invoice_edit_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


