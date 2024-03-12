# UnibeeApiBeanCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**scale** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_currency import UnibeeApiBeanCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanCurrency from a JSON string
unibee_api_bean_currency_instance = UnibeeApiBeanCurrency.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanCurrency.to_json()

# convert the object into a dict
unibee_api_bean_currency_dict = unibee_api_bean_currency_instance.to_dict()
# create an instance of UnibeeApiBeanCurrency from a dict
unibee_api_bean_currency_form_dict = unibee_api_bean_currency.from_dict(unibee_api_bean_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


