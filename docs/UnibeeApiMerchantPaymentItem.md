# UnibeeApiMerchantPaymentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**image_url** | **str** | ImageUrl | [optional] 
**product_url** | **str** | ProductUrl | [optional] 
**quantity** | **int** | Quantity | 
**tax_scale** | **int** | TaxScale | 
**unit_amount_excluding_tax** | **int** | UnitAmountExcludingTax | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_item import UnibeeApiMerchantPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentItem from a JSON string
unibee_api_merchant_payment_item_instance = UnibeeApiMerchantPaymentItem.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentItem.to_json()

# convert the object into a dict
unibee_api_merchant_payment_item_dict = unibee_api_merchant_payment_item_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentItem from a dict
unibee_api_merchant_payment_item_form_dict = unibee_api_merchant_payment_item.from_dict(unibee_api_merchant_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


