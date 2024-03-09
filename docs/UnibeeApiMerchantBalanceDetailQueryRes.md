# UnibeeApiMerchantBalanceDetailQueryRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | [**List[UnibeeInternalLogicGatewayRoGatewayBalance]**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 
**connect_reserved** | [**List[UnibeeInternalLogicGatewayRoGatewayBalance]**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 
**pending** | [**List[UnibeeInternalLogicGatewayRoGatewayBalance]**](UnibeeInternalLogicGatewayRoGatewayBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_balance_detail_query_res import UnibeeApiMerchantBalanceDetailQueryRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantBalanceDetailQueryRes from a JSON string
unibee_api_merchant_balance_detail_query_res_instance = UnibeeApiMerchantBalanceDetailQueryRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantBalanceDetailQueryRes.to_json()

# convert the object into a dict
unibee_api_merchant_balance_detail_query_res_dict = unibee_api_merchant_balance_detail_query_res_instance.to_dict()
# create an instance of UnibeeApiMerchantBalanceDetailQueryRes from a dict
unibee_api_merchant_balance_detail_query_res_form_dict = unibee_api_merchant_balance_detail_query_res.from_dict(unibee_api_merchant_balance_detail_query_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


