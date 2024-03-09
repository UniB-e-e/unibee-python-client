# MerchantBalanceUserBalanceQueryGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**UnibeeInternalLogicGatewayRoGatewayBalance**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 
**cash_balance** | [**List[UnibeeInternalLogicGatewayRoGatewayBalance]**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 
**invoice_credit_balance** | [**List[UnibeeInternalLogicGatewayRoGatewayBalance]**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_balance_user_balance_query_get200_response_data import MerchantBalanceUserBalanceQueryGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBalanceUserBalanceQueryGet200ResponseData from a JSON string
merchant_balance_user_balance_query_get200_response_data_instance = MerchantBalanceUserBalanceQueryGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantBalanceUserBalanceQueryGet200ResponseData.to_json()

# convert the object into a dict
merchant_balance_user_balance_query_get200_response_data_dict = merchant_balance_user_balance_query_get200_response_data_instance.to_dict()
# create an instance of MerchantBalanceUserBalanceQueryGet200ResponseData from a dict
merchant_balance_user_balance_query_get200_response_data_form_dict = merchant_balance_user_balance_query_get200_response_data.from_dict(merchant_balance_user_balance_query_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


