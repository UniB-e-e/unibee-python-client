# UnibeeInternalModelEntityOverseaPayInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biz_type** | **int** | biz type from payment 1-single payment, 3-subscription | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**data** | **str** | data (json) | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_invoice_id** | **str** |  | [optional] 
**gateway_invoice_pdf** | **str** |  | [optional] 
**gateway_payment_id** | **str** |  | [optional] 
**gateway_status** | **str** |  | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**id** | **int** |  | [optional] 
**invoice_id** | **str** | invoice_id | [optional] 
**invoice_name** | **str** | invoice name | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**lines** | **str** | lines( json) | [optional] 
**link** | **str** | invoice link | [optional] 
**merchant_id** | **int** | merchant_id | [optional] 
**payment_id** | **str** | paymentId | [optional] 
**payment_link** | **str** | invoice payment link | [optional] 
**period_end** | **int** | period_end utc time | [optional] 
**period_end_time** | **str** |  | [optional] 
**period_start** | **int** | period_start, utc time | [optional] 
**period_start_time** | **str** |  | [optional] 
**refund_id** | **str** | refundId | [optional] 
**send_email** | **str** | email | [optional] 
**send_note** | **str** | send_note | [optional] 
**send_pdf** | **str** | pdf link | [optional] 
**send_status** | **int** | email send status，0-No | 1- YES | [optional] 
**send_terms** | **str** | send_terms | [optional] 
**status** | **int** | status，0-Init | 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled | [optional] 
**subscription_amount** | **int** | sub amount,cent | [optional] 
**subscription_amount_excluding_tax** | **int** |  | [optional] 
**subscription_id** | **str** | subscription_id | [optional] 
**tax_amount** | **int** | tax amount,cent | [optional] 
**tax_scale** | **int** | Tax scale，1000 &#x3D; 10% | [optional] 
**total_amount** | **int** | total amount, cent | [optional] 
**total_amount_excluding_tax** | **int** |  | [optional] 
**unique_id** | **str** | unique_id | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_invoice import UnibeeInternalModelEntityOverseaPayInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayInvoice from a JSON string
unibee_internal_model_entity_oversea_pay_invoice_instance = UnibeeInternalModelEntityOverseaPayInvoice.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayInvoice.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_invoice_dict = unibee_internal_model_entity_oversea_pay_invoice_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayInvoice from a dict
unibee_internal_model_entity_oversea_pay_invoice_form_dict = unibee_internal_model_entity_oversea_pay_invoice.from_dict(unibee_internal_model_entity_oversea_pay_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


