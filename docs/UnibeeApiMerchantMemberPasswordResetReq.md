# UnibeeApiMerchantMemberPasswordResetReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** | NewPassword | 
**old_password** | **str** | OldPassword | 

## Example

```python
from openapi_client.models.unibee_api_merchant_member_password_reset_req import UnibeeApiMerchantMemberPasswordResetReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMemberPasswordResetReq from a JSON string
unibee_api_merchant_member_password_reset_req_instance = UnibeeApiMerchantMemberPasswordResetReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMemberPasswordResetReq.to_json()

# convert the object into a dict
unibee_api_merchant_member_password_reset_req_dict = unibee_api_merchant_member_password_reset_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMemberPasswordResetReq from a dict
unibee_api_merchant_member_password_reset_req_form_dict = unibee_api_merchant_member_password_reset_req.from_dict(unibee_api_merchant_member_password_reset_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


