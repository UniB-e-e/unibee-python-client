# UnibeeApiMerchantVatSetupGatewayReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | IsDefault, default is true | [optional] [default to True]
**data** | **str** | Data | 
**gateway_name** | **str** | GatewayName, em. vatsense | 

## Example

```python
from openapi_client.models.unibee_api_merchant_vat_setup_gateway_req import UnibeeApiMerchantVatSetupGatewayReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantVatSetupGatewayReq from a JSON string
unibee_api_merchant_vat_setup_gateway_req_instance = UnibeeApiMerchantVatSetupGatewayReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantVatSetupGatewayReq.to_json()

# convert the object into a dict
unibee_api_merchant_vat_setup_gateway_req_dict = unibee_api_merchant_vat_setup_gateway_req_instance.to_dict()
# create an instance of UnibeeApiMerchantVatSetupGatewayReq from a dict
unibee_api_merchant_vat_setup_gateway_req_form_dict = unibee_api_merchant_vat_setup_gateway_req.from_dict(unibee_api_merchant_vat_setup_gateway_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


