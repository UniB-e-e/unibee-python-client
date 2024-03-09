# UnibeeInternalLogicGatewayRoInvoiceDetailRo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency | [optional] 
**data** | **str** | Data | [optional] 
**discount_amount** | **int** | DiscountAmount,Cents | [optional] 
**gateway** | [**UnibeeInternalLogicGatewayRoGatewaySimplify**](UnibeeInternalLogicGatewayRoGatewaySimplify.md) |  | [optional] 
**gateway_id** | **int** | Id | [optional] 
**gateway_invoice_id** | **str** | GatewayInvoiceId | [optional] 
**gateway_invoice_pdf** | **str** | GatewayInvoicePdf pdf | [optional] 
**gateway_payment_id** | **str** | GatewayPaymentId PaymentId | [optional] 
**gateway_status** | **str** | GatewayStatus，Stripe：https://stripe.com/docs/api/invoices/object | [optional] 
**gateway_user_id** | **str** | GatewayUserId Id | [optional] 
**gmt_create** | **str** | GmtCreate | [optional] 
**gmt_modify** | **str** | GmtModify | [optional] 
**id** | **int** |  | [optional] 
**invoice_id** | **str** | InvoiceId | [optional] 
**invoice_name** | **str** | InvoiceName | [optional] 
**is_deleted** | **int** |  | [optional] 
**lines** | [**List[UnibeeInternalLogicGatewayRoInvoiceItemDetailRo]**](UnibeeInternalLogicGatewayRoInvoiceItemDetailRo.md) | lines json data | [optional] 
**link** | **str** | Link | [optional] 
**merchant** | [**UnibeeInternalModelEntityOverseaPayMerchant**](UnibeeInternalModelEntityOverseaPayMerchant.md) |  | [optional] 
**merchant_id** | **int** | MerchantId | [optional] 
**payment** | [**UnibeeInternalModelEntityOverseaPayPayment**](UnibeeInternalModelEntityOverseaPayPayment.md) |  | [optional] 
**payment_id** | **str** | PaymentId | [optional] 
**period_end** | **int** | period_end | [optional] 
**period_start** | **int** | period_start | [optional] 
**refund** | [**UnibeeInternalModelEntityOverseaPayRefund**](UnibeeInternalModelEntityOverseaPayRefund.md) |  | [optional] 
**refund_id** | **str** | refundId | [optional] 
**send_email** | **str** | SendEmail | [optional] 
**send_note** | **str** | SendNote | [optional] 
**send_pdf** | **str** | SendPdf | [optional] 
**send_status** | **int** | SendStatus，0-No | 1- YES | [optional] 
**send_terms** | **str** | SendTerms | [optional] 
**status** | **int** | Status，0-Init | 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled | [optional] 
**subscription** | [**UnibeeInternalModelEntityOverseaPaySubscription**](UnibeeInternalModelEntityOverseaPaySubscription.md) |  | [optional] 
**subscription_amount** | **int** | SubscriptionAmount,Cents | [optional] 
**subscription_amount_excluding_tax** | **int** | SubscriptionAmountExcludingTax,Cents | [optional] 
**subscription_id** | **str** | SubscriptionId | [optional] 
**tax_amount** | **int** | TaxAmount,Cents | [optional] 
**tax_scale** | **int** | TaxScale，1000 &#x3D; 10% | [optional] 
**total_amount** | **int** | TotalAmount,Cents | [optional] 
**total_amount_excluding_tax** | **int** | TotalAmountExcludingTax,Cents | [optional] 
**unique_id** | **str** | UniqueId | [optional] 
**user_account** | [**UnibeeInternalModelEntityOverseaPayUserAccount**](UnibeeInternalModelEntityOverseaPayUserAccount.md) |  | [optional] 
**user_id** | **int** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_invoice_detail_ro import UnibeeInternalLogicGatewayRoInvoiceDetailRo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailRo from a JSON string
unibee_internal_logic_gateway_ro_invoice_detail_ro_instance = UnibeeInternalLogicGatewayRoInvoiceDetailRo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoInvoiceDetailRo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_invoice_detail_ro_dict = unibee_internal_logic_gateway_ro_invoice_detail_ro_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoInvoiceDetailRo from a dict
unibee_internal_logic_gateway_ro_invoice_detail_ro_form_dict = unibee_internal_logic_gateway_ro_invoice_detail_ro.from_dict(unibee_internal_logic_gateway_ro_invoice_detail_ro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


