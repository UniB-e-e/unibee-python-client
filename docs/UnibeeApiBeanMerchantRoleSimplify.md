# UnibeeApiBeanMerchantRoleSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**id** | **int** | userId | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**permissions** | [**List[UnibeeApiBeanMerchantRolePermission]**](UnibeeApiBeanMerchantRolePermission.md) | permissions | [optional] 
**role** | **str** | role | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_role_simplify import UnibeeApiBeanMerchantRoleSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantRoleSimplify from a JSON string
unibee_api_bean_merchant_role_simplify_instance = UnibeeApiBeanMerchantRoleSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantRoleSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_role_simplify_dict = unibee_api_bean_merchant_role_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantRoleSimplify from a dict
unibee_api_bean_merchant_role_simplify_form_dict = unibee_api_bean_merchant_role_simplify.from_dict(unibee_api_bean_merchant_role_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


