# MerchantUserListGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**MerchantUserListGet200ResponseData**](MerchantUserListGet200ResponseData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**redirect** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_user_list_get200_response import MerchantUserListGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantUserListGet200Response from a JSON string
merchant_user_list_get200_response_instance = MerchantUserListGet200Response.from_json(json)
# print the JSON string representation of the object
print MerchantUserListGet200Response.to_json()

# convert the object into a dict
merchant_user_list_get200_response_dict = merchant_user_list_get200_response_instance.to_dict()
# create an instance of MerchantUserListGet200Response from a dict
merchant_user_list_get200_response_form_dict = merchant_user_list_get200_response.from_dict(merchant_user_list_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


