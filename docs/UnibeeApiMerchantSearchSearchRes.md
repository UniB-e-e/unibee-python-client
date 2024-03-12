# UnibeeApiMerchantSearchSearchRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_invoice** | [**List[UnibeeApiBeanInvoiceSimplify]**](UnibeeApiBeanInvoiceSimplify.md) | MatchInvoice | [optional] 
**match_user_accounts** | [**List[UnibeeApiBeanUserAccountSimplify]**](UnibeeApiBeanUserAccountSimplify.md) | MatchUserAccounts | [optional] 
**precision_match_object** | [**UnibeeApiMerchantSearchPrecisionMatchObject**](UnibeeApiMerchantSearchPrecisionMatchObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_search_search_res import UnibeeApiMerchantSearchSearchRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSearchSearchRes from a JSON string
unibee_api_merchant_search_search_res_instance = UnibeeApiMerchantSearchSearchRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSearchSearchRes.to_json()

# convert the object into a dict
unibee_api_merchant_search_search_res_dict = unibee_api_merchant_search_search_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSearchSearchRes from a dict
unibee_api_merchant_search_search_res_form_dict = unibee_api_merchant_search_search_res.from_dict(unibee_api_merchant_search_search_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


