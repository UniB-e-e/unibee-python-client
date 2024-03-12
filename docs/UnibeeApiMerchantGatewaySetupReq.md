# UnibeeApiMerchantGatewaySetupReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_key** | **str** | GatewayKey | [optional] 
**gateway_name** | **str** | GatewayName, stripe|paypal|changelly | 
**gateway_secret** | **str** | GatewaySecret | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_gateway_setup_req import UnibeeApiMerchantGatewaySetupReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantGatewaySetupReq from a JSON string
unibee_api_merchant_gateway_setup_req_instance = UnibeeApiMerchantGatewaySetupReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantGatewaySetupReq.to_json()

# convert the object into a dict
unibee_api_merchant_gateway_setup_req_dict = unibee_api_merchant_gateway_setup_req_instance.to_dict()
# create an instance of UnibeeApiMerchantGatewaySetupReq from a dict
unibee_api_merchant_gateway_setup_req_form_dict = unibee_api_merchant_gateway_setup_req.from_dict(unibee_api_merchant_gateway_setup_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


