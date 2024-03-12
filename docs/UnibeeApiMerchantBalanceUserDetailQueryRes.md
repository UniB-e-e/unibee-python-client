# UnibeeApiMerchantBalanceUserDetailQueryRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | [**UnibeeInternalLogicGatewayGatewayBeanGatewayBalance**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 
**cash_balance** | [**List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 
**invoice_credit_balance** | [**List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]**](UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_balance_user_detail_query_res import UnibeeApiMerchantBalanceUserDetailQueryRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantBalanceUserDetailQueryRes from a JSON string
unibee_api_merchant_balance_user_detail_query_res_instance = UnibeeApiMerchantBalanceUserDetailQueryRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantBalanceUserDetailQueryRes.to_json()

# convert the object into a dict
unibee_api_merchant_balance_user_detail_query_res_dict = unibee_api_merchant_balance_user_detail_query_res_instance.to_dict()
# create an instance of UnibeeApiMerchantBalanceUserDetailQueryRes from a dict
unibee_api_merchant_balance_user_detail_query_res_form_dict = unibee_api_merchant_balance_user_detail_query_res.from_dict(unibee_api_merchant_balance_user_detail_query_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


