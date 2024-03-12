# UnibeeApiBeanVatCountryRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 
**id** | **int** | TaxId | [optional] 
**standard_tax_percentage** | **int** | Tax税率，万分位，1000 表示 10% | [optional] 
**vat_support** | **bool** | vat support,true or false | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_vat_country_rate import UnibeeApiBeanVatCountryRate

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanVatCountryRate from a JSON string
unibee_api_bean_vat_country_rate_instance = UnibeeApiBeanVatCountryRate.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanVatCountryRate.to_json()

# convert the object into a dict
unibee_api_bean_vat_country_rate_dict = unibee_api_bean_vat_country_rate_instance.to_dict()
# create an instance of UnibeeApiBeanVatCountryRate from a dict
unibee_api_bean_vat_country_rate_form_dict = unibee_api_bean_vat_country_rate.from_dict(unibee_api_bean_vat_country_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


