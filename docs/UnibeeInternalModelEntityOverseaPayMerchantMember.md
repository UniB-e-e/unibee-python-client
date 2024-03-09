# UnibeeInternalModelEntityOverseaPayMerchantMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | email | [optional] 
**first_name** | **str** | first name | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**id** | **int** | userId | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**last_name** | **str** | last name | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**mobile** | **str** | mobile | [optional] 
**password** | **str** | password | [optional] 
**user_name** | **str** | user name | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_merchant_member import UnibeeInternalModelEntityOverseaPayMerchantMember

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayMerchantMember from a JSON string
unibee_internal_model_entity_oversea_pay_merchant_member_instance = UnibeeInternalModelEntityOverseaPayMerchantMember.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayMerchantMember.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_merchant_member_dict = unibee_internal_model_entity_oversea_pay_merchant_member_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayMerchantMember from a dict
unibee_internal_model_entity_oversea_pay_merchant_member_form_dict = unibee_internal_model_entity_oversea_pay_merchant_member.from_dict(unibee_internal_model_entity_oversea_pay_merchant_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


