# UnibeeApiMerchantAuthLoginReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | 
**password** | **str** | Password | 

## Example

```python
from openapi_client.models.unibee_api_merchant_auth_login_req import UnibeeApiMerchantAuthLoginReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantAuthLoginReq from a JSON string
unibee_api_merchant_auth_login_req_instance = UnibeeApiMerchantAuthLoginReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantAuthLoginReq.to_json()

# convert the object into a dict
unibee_api_merchant_auth_login_req_dict = unibee_api_merchant_auth_login_req_instance.to_dict()
# create an instance of UnibeeApiMerchantAuthLoginReq from a dict
unibee_api_merchant_auth_login_req_form_dict = unibee_api_merchant_auth_login_req.from_dict(unibee_api_merchant_auth_login_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


