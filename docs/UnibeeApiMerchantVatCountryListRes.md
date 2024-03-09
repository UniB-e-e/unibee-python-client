# UnibeeApiMerchantVatCountryListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vat_country_list** | [**List[UnibeeInternalLogicGatewayRoVatCountryRate]**](UnibeeInternalLogicGatewayRoVatCountryRate.md) | VatCountryList | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_vat_country_list_res import UnibeeApiMerchantVatCountryListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantVatCountryListRes from a JSON string
unibee_api_merchant_vat_country_list_res_instance = UnibeeApiMerchantVatCountryListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantVatCountryListRes.to_json()

# convert the object into a dict
unibee_api_merchant_vat_country_list_res_dict = unibee_api_merchant_vat_country_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantVatCountryListRes from a dict
unibee_api_merchant_vat_country_list_res_form_dict = unibee_api_merchant_vat_country_list_res.from_dict(unibee_api_merchant_vat_country_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


