# MerchantSearchKeySearchGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_invoice** | [**List[UnibeeInternalModelEntityOverseaPayInvoice]**](UnibeeInternalModelEntityOverseaPayInvoice.md) | MatchInvoice | [optional] 
**match_user_accounts** | [**List[UnibeeInternalModelEntityOverseaPayUserAccount]**](UnibeeInternalModelEntityOverseaPayUserAccount.md) | MatchUserAccounts | [optional] 
**precision_match_object** | [**UnibeeApiMerchantSearchPrecisionMatchObject**](UnibeeApiMerchantSearchPrecisionMatchObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_search_key_search_get200_response_data import MerchantSearchKeySearchGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSearchKeySearchGet200ResponseData from a JSON string
merchant_search_key_search_get200_response_data_instance = MerchantSearchKeySearchGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSearchKeySearchGet200ResponseData.to_json()

# convert the object into a dict
merchant_search_key_search_get200_response_data_dict = merchant_search_key_search_get200_response_data_instance.to_dict()
# create an instance of MerchantSearchKeySearchGet200ResponseData from a dict
merchant_search_key_search_get200_response_data_form_dict = merchant_search_key_search_get200_response_data.from_dict(merchant_search_key_search_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


