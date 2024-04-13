# MerchantRoleListGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_roles** | [**List[UnibeeApiBeanMerchantRoleSimplify]**](UnibeeApiBeanMerchantRoleSimplify.md) | Merchant Roles | [optional] 

## Example

```python
from openapi_client.models.merchant_role_list_get200_response_data import MerchantRoleListGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantRoleListGet200ResponseData from a JSON string
merchant_role_list_get200_response_data_instance = MerchantRoleListGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantRoleListGet200ResponseData.to_json()

# convert the object into a dict
merchant_role_list_get200_response_data_dict = merchant_role_list_get200_response_data_instance.to_dict()
# create an instance of MerchantRoleListGet200ResponseData from a dict
merchant_role_list_get200_response_data_form_dict = merchant_role_list_get200_response_data.from_dict(merchant_role_list_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


