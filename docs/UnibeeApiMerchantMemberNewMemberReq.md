# UnibeeApiMerchantMemberNewMemberReq

Will send email to member email provided, member can enter admin portal by email otp login

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email, email of member, member otp login needs | 
**first_name** | **str** | FirstName, member firstName, invoice needs | [optional] 
**last_name** | **str** | LastName, member firstName, invoice needs | [optional] 
**role** | **str** | Role, permission role of member | 

## Example

```python
from openapi_client.models.unibee_api_merchant_member_new_member_req import UnibeeApiMerchantMemberNewMemberReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMemberNewMemberReq from a JSON string
unibee_api_merchant_member_new_member_req_instance = UnibeeApiMerchantMemberNewMemberReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMemberNewMemberReq.to_json()

# convert the object into a dict
unibee_api_merchant_member_new_member_req_dict = unibee_api_merchant_member_new_member_req_instance.to_dict()
# create an instance of UnibeeApiMerchantMemberNewMemberReq from a dict
unibee_api_merchant_member_new_member_req_form_dict = unibee_api_merchant_member_new_member_req.from_dict(unibee_api_merchant_member_new_member_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


