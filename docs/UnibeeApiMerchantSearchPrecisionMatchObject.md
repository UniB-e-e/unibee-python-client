# UnibeeApiMerchantSearchPrecisionMatchObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** | match Id user_id|invoice_id | [optional] 
**type** | **str** | match Type, user|invoice | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_search_precision_match_object import UnibeeApiMerchantSearchPrecisionMatchObject

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSearchPrecisionMatchObject from a JSON string
unibee_api_merchant_search_precision_match_object_instance = UnibeeApiMerchantSearchPrecisionMatchObject.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSearchPrecisionMatchObject.to_json()

# convert the object into a dict
unibee_api_merchant_search_precision_match_object_dict = unibee_api_merchant_search_precision_match_object_instance.to_dict()
# create an instance of UnibeeApiMerchantSearchPrecisionMatchObject from a dict
unibee_api_merchant_search_precision_match_object_form_dict = unibee_api_merchant_search_precision_match_object.from_dict(unibee_api_merchant_search_precision_match_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


