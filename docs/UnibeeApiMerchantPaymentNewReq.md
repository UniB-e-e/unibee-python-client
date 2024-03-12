# UnibeeApiMerchantPaymentNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | CountryCode | [optional] 
**currency** | **str** | Currency | 
**email** | **str** | Email | 
**external_payment_id** | **str** | ExternalPaymentId should unique for payment | 
**external_user_id** | **str** | ExternalUserId, should unique for user | 
**gas_payer** | **str** | who pay the gas, merchant|user | [optional] 
**gateway_id** | **int** | GatewayId | 
**items** | [**List[UnibeeApiMerchantPaymentItem]**](UnibeeApiMerchantPaymentItem.md) | Items | [optional] 
**metadata** | **Dict[str, str]** | Metadata，Map | [optional] 
**redirect_url** | **str** | Redirect Url | [optional] 
**total_amount** | **int** | Total PaymentAmount, Cent | 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_new_req import UnibeeApiMerchantPaymentNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentNewReq from a JSON string
unibee_api_merchant_payment_new_req_instance = UnibeeApiMerchantPaymentNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_new_req_dict = unibee_api_merchant_payment_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentNewReq from a dict
unibee_api_merchant_payment_new_req_form_dict = unibee_api_merchant_payment_new_req.from_dict(unibee_api_merchant_payment_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


