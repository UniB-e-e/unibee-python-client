# MerchantCountryConfigListPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[UnibeeApiBeanMerchantCountryConfigSimplify]**](UnibeeApiBeanMerchantCountryConfigSimplify.md) | Configs | [optional] 

## Example

```python
from openapi_client.models.merchant_country_config_list_post200_response_data import MerchantCountryConfigListPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantCountryConfigListPost200ResponseData from a JSON string
merchant_country_config_list_post200_response_data_instance = MerchantCountryConfigListPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantCountryConfigListPost200ResponseData.to_json()

# convert the object into a dict
merchant_country_config_list_post200_response_data_dict = merchant_country_config_list_post200_response_data_instance.to_dict()
# create an instance of MerchantCountryConfigListPost200ResponseData from a dict
merchant_country_config_list_post200_response_data_form_dict = merchant_country_config_list_post200_response_data.from_dict(merchant_country_config_list_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


