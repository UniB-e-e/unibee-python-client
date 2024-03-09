# UnibeeApiMerchantAuthRegisterReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**password** | **str** | Password | 
**phone** | **str** | Phone | [optional] 
**user_name** | **str** | UserName | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_auth_register_req import UnibeeApiMerchantAuthRegisterReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantAuthRegisterReq from a JSON string
unibee_api_merchant_auth_register_req_instance = UnibeeApiMerchantAuthRegisterReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantAuthRegisterReq.to_json()

# convert the object into a dict
unibee_api_merchant_auth_register_req_dict = unibee_api_merchant_auth_register_req_instance.to_dict()
# create an instance of UnibeeApiMerchantAuthRegisterReq from a dict
unibee_api_merchant_auth_register_req_form_dict = unibee_api_merchant_auth_register_req.from_dict(unibee_api_merchant_auth_register_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


