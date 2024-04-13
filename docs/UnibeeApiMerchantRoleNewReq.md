# UnibeeApiMerchantRoleNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[UnibeeApiBeanMerchantRolePermission]**](UnibeeApiBeanMerchantRolePermission.md) | Permissions | 
**role** | **str** | Role | 

## Example

```python
from openapi_client.models.unibee_api_merchant_role_new_req import UnibeeApiMerchantRoleNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantRoleNewReq from a JSON string
unibee_api_merchant_role_new_req_instance = UnibeeApiMerchantRoleNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantRoleNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_role_new_req_dict = unibee_api_merchant_role_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantRoleNewReq from a dict
unibee_api_merchant_role_new_req_form_dict = unibee_api_merchant_role_new_req.from_dict(unibee_api_merchant_role_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


