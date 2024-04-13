# UnibeeApiMerchantMemberUpdateMemberRoleReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **int** | MemberId | [optional] 
**role** | **str** | Role | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_member_update_member_role_req import UnibeeApiMerchantMemberUpdateMemberRoleReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMemberUpdateMemberRoleReq from a JSON string
unibee_api_merchant_member_update_member_role_req_instance = UnibeeApiMerchantMemberUpdateMemberRoleReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMemberUpdateMemberRoleReq.to_json()

# convert the object into a dict
unibee_api_merchant_member_update_member_role_req_dict = unibee_api_merchant_member_update_member_role_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMemberUpdateMemberRoleReq from a dict
unibee_api_merchant_member_update_member_role_req_form_dict = unibee_api_merchant_member_update_member_role_req.from_dict(unibee_api_merchant_member_update_member_role_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


