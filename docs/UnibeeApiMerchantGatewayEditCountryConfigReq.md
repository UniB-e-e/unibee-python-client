# UnibeeApiMerchantGatewayEditCountryConfigReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_config** | **Dict[str, bool]** | CountryConfig | [optional] 
**gateway_id** | **int** | GatewayId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_gateway_edit_country_config_req import UnibeeApiMerchantGatewayEditCountryConfigReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantGatewayEditCountryConfigReq from a JSON string
unibee_api_merchant_gateway_edit_country_config_req_instance = UnibeeApiMerchantGatewayEditCountryConfigReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantGatewayEditCountryConfigReq.to_json()

# convert the object into a dict
unibee_api_merchant_gateway_edit_country_config_req_dict = unibee_api_merchant_gateway_edit_country_config_req_instance.to_dict()
# create an instance of UnibeeApiMerchantGatewayEditCountryConfigReq from a dict
unibee_api_merchant_gateway_edit_country_config_req_form_dict = unibee_api_merchant_gateway_edit_country_config_req.from_dict(unibee_api_merchant_gateway_edit_country_config_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


