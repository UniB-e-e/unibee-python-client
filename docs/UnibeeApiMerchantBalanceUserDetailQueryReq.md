# UnibeeApiMerchantBalanceUserDetailQueryReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **int** | gatewayId | 
**user_id** | **int** | userId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_balance_user_detail_query_req import UnibeeApiMerchantBalanceUserDetailQueryReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantBalanceUserDetailQueryReq from a JSON string
unibee_api_merchant_balance_user_detail_query_req_instance = UnibeeApiMerchantBalanceUserDetailQueryReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantBalanceUserDetailQueryReq.to_json()

# convert the object into a dict
unibee_api_merchant_balance_user_detail_query_req_dict = unibee_api_merchant_balance_user_detail_query_req_instance.to_dict()
# create an instance of UnibeeApiMerchantBalanceUserDetailQueryReq from a dict
unibee_api_merchant_balance_user_detail_query_req_form_dict = unibee_api_merchant_balance_user_detail_query_req.from_dict(unibee_api_merchant_balance_user_detail_query_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


