# UnibeeApiMerchantEmailGatewaySetupReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | IsDefault, default is true | [optional] [default to True]
**data** | **str** | data | 
**gateway_name** | **str** | GatewayName, e.m. sendgrid | 

## Example

```python
from openapi_client.models.unibee_api_merchant_email_gateway_setup_req import UnibeeApiMerchantEmailGatewaySetupReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantEmailGatewaySetupReq from a JSON string
unibee_api_merchant_email_gateway_setup_req_instance = UnibeeApiMerchantEmailGatewaySetupReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantEmailGatewaySetupReq.to_json()

# convert the object into a dict
unibee_api_merchant_email_gateway_setup_req_dict = unibee_api_merchant_email_gateway_setup_req_instance.to_dict()
# create an instance of UnibeeApiMerchantEmailGatewaySetupReq from a dict
unibee_api_merchant_email_gateway_setup_req_form_dict = unibee_api_merchant_email_gateway_setup_req.from_dict(unibee_api_merchant_email_gateway_setup_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


