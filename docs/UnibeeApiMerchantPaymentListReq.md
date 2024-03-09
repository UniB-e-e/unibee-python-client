# UnibeeApiMerchantPaymentListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**country_code** | **str** | CountryCode | [optional] 
**currency** | **str** | Currency | [optional] 
**email** | **str** | Email | [optional] 
**gateway_id** | **int** | GatewayId | [optional] 
**page** | **int** | Page, Start With 0 | [optional] 
**sort_field** | **str** | Sort Field，user_id|create_time|status | [optional] 
**sort_type** | **str** | Sort Type，asc|desc | [optional] 
**status** | **int** | Status, 10-Created|20-Success|30-Failed|40-Cancelled | [optional] 
**user_id** | **int** | UserId  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_list_req import UnibeeApiMerchantPaymentListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentListReq from a JSON string
unibee_api_merchant_payment_list_req_instance = UnibeeApiMerchantPaymentListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentListReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_list_req_dict = unibee_api_merchant_payment_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentListReq from a dict
unibee_api_merchant_payment_list_req_form_dict = unibee_api_merchant_payment_list_req.from_dict(unibee_api_merchant_payment_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


