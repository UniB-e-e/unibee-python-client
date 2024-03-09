# UnibeeApiMerchantPaymentRefundListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency | [optional] 
**email** | **str** | Email | [optional] 
**gateway_id** | **int** | GatewayId | [optional] 
**payment_id** | **str** | PaymentId | 
**status** | **int** | Status,10-create|20-success|30-Failed|40-Reverse | [optional] 
**user_id** | **int** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_refund_list_req import UnibeeApiMerchantPaymentRefundListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentRefundListReq from a JSON string
unibee_api_merchant_payment_refund_list_req_instance = UnibeeApiMerchantPaymentRefundListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentRefundListReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_refund_list_req_dict = unibee_api_merchant_payment_refund_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentRefundListReq from a dict
unibee_api_merchant_payment_refund_list_req_form_dict = unibee_api_merchant_payment_refund_list_req.from_dict(unibee_api_merchant_payment_refund_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


