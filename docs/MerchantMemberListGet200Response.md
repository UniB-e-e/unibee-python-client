# MerchantMemberListGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**MerchantMemberListGet200ResponseData**](MerchantMemberListGet200ResponseData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**redirect** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_member_list_get200_response import MerchantMemberListGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMemberListGet200Response from a JSON string
merchant_member_list_get200_response_instance = MerchantMemberListGet200Response.from_json(json)
# print the JSON string representation of the object
print MerchantMemberListGet200Response.to_json()

# convert the object into a dict
merchant_member_list_get200_response_dict = merchant_member_list_get200_response_instance.to_dict()
# create an instance of MerchantMemberListGet200Response from a dict
merchant_member_list_get200_response_form_dict = merchant_member_list_get200_response.from_dict(merchant_member_list_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


