# MerchantBalanceMerchantBalanceQueryGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 
**connect_reserved** | [**List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 
**pending** | [**List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_balance_merchant_balance_query_get200_response_data import MerchantBalanceMerchantBalanceQueryGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBalanceMerchantBalanceQueryGet200ResponseData from a JSON string
merchant_balance_merchant_balance_query_get200_response_data_instance = MerchantBalanceMerchantBalanceQueryGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantBalanceMerchantBalanceQueryGet200ResponseData.to_json()

# convert the object into a dict
merchant_balance_merchant_balance_query_get200_response_data_dict = merchant_balance_merchant_balance_query_get200_response_data_instance.to_dict()
# create an instance of MerchantBalanceMerchantBalanceQueryGet200ResponseData from a dict
merchant_balance_merchant_balance_query_get200_response_data_form_dict = merchant_balance_merchant_balance_query_get200_response_data.from_dict(merchant_balance_merchant_balance_query_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


