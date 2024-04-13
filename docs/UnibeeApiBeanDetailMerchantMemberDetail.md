# UnibeeApiBeanDetailMerchantMemberDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | email | [optional] 
**first_name** | **str** | first name | [optional] 
**id** | **int** | userId | [optional] 
**last_name** | **str** | last name | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**mobile** | **str** | mobile | [optional] 
**permissions** | [**List[UnibeeApiBeanMerchantRolePermission]**](UnibeeApiBeanMerchantRolePermission.md) | permissions | [optional] 
**role** | **str** | role | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_detail_merchant_member_detail import UnibeeApiBeanDetailMerchantMemberDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanDetailMerchantMemberDetail from a JSON string
unibee_api_bean_detail_merchant_member_detail_instance = UnibeeApiBeanDetailMerchantMemberDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanDetailMerchantMemberDetail.to_json()

# convert the object into a dict
unibee_api_bean_detail_merchant_member_detail_dict = unibee_api_bean_detail_merchant_member_detail_instance.to_dict()
# create an instance of UnibeeApiBeanDetailMerchantMemberDetail from a dict
unibee_api_bean_detail_merchant_member_detail_form_dict = unibee_api_bean_detail_merchant_member_detail.from_dict(unibee_api_bean_detail_merchant_member_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


