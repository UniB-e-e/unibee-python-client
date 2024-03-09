# UnibeeApiMerchantSearchSearchReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_key** | **str** | SearchKey, Will Search UserId|Email|UserName|CompanyName|SubscriptionId|VatNumber|InvoiceId||PaymentId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_search_search_req import UnibeeApiMerchantSearchSearchReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSearchSearchReq from a JSON string
unibee_api_merchant_search_search_req_instance = UnibeeApiMerchantSearchSearchReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSearchSearchReq.to_json()

# convert the object into a dict
unibee_api_merchant_search_search_req_dict = unibee_api_merchant_search_search_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSearchSearchReq from a dict
unibee_api_merchant_search_search_req_form_dict = unibee_api_merchant_search_search_req.from_dict(unibee_api_merchant_search_search_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


