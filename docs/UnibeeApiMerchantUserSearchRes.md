# UnibeeApiMerchantUserSearchRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_accounts** | [**List[UnibeeApiBeanUserAccountSimplify]**](UnibeeApiBeanUserAccountSimplify.md) | UserAccounts | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_user_search_res import UnibeeApiMerchantUserSearchRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantUserSearchRes from a JSON string
unibee_api_merchant_user_search_res_instance = UnibeeApiMerchantUserSearchRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantUserSearchRes.to_json()

# convert the object into a dict
unibee_api_merchant_user_search_res_dict = unibee_api_merchant_user_search_res_instance.to_dict()
# create an instance of UnibeeApiMerchantUserSearchRes from a dict
unibee_api_merchant_user_search_res_form_dict = unibee_api_merchant_user_search_res.from_dict(unibee_api_merchant_user_search_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


