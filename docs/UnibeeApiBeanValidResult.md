# UnibeeApiBeanValidResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_address** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 
**validate_message** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_valid_result import UnibeeApiBeanValidResult

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanValidResult from a JSON string
unibee_api_bean_valid_result_instance = UnibeeApiBeanValidResult.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanValidResult.to_json()

# convert the object into a dict
unibee_api_bean_valid_result_dict = unibee_api_bean_valid_result_instance.to_dict()
# create an instance of UnibeeApiBeanValidResult from a dict
unibee_api_bean_valid_result_form_dict = unibee_api_bean_valid_result.from_dict(unibee_api_bean_valid_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


