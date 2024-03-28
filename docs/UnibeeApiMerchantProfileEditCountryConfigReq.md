# UnibeeApiMerchantProfileEditCountryConfigReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | CountryCode | 
**name** | **str** | name | [optional] 
**vat_enable** | **bool** | VatEnable, Default true | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_profile_edit_country_config_req import UnibeeApiMerchantProfileEditCountryConfigReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantProfileEditCountryConfigReq from a JSON string
unibee_api_merchant_profile_edit_country_config_req_instance = UnibeeApiMerchantProfileEditCountryConfigReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantProfileEditCountryConfigReq.to_json()

# convert the object into a dict
unibee_api_merchant_profile_edit_country_config_req_dict = unibee_api_merchant_profile_edit_country_config_req_instance.to_dict()
# create an instance of UnibeeApiMerchantProfileEditCountryConfigReq from a dict
unibee_api_merchant_profile_edit_country_config_req_form_dict = unibee_api_merchant_profile_edit_country_config_req.from_dict(unibee_api_merchant_profile_edit_country_config_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


