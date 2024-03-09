# UnibeeInternalModelEntityOverseaPayMerchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | [optional] 
**api_key** | **str** | merchant open api key | [optional] 
**business_num** | **str** | business_num | [optional] 
**company_id** | **int** | company_id | [optional] 
**company_logo** | **str** | company_logo | [optional] 
**company_name** | **str** | company_name | [optional] 
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | email | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update_time | [optional] 
**home_url** | **str** |  | [optional] 
**host** | **str** | merchant user portal host | [optional] 
**id** | **int** | merchant_id | [optional] 
**idcard** | **str** | idcard | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**location** | **str** | location | [optional] 
**name** | **str** | name | [optional] 
**phone** | **str** | phone | [optional] 
**time_zone** | **str** | merchant default time zone | [optional] 
**type** | **int** | type | [optional] 
**user_id** | **int** | create_user_id | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_merchant import UnibeeInternalModelEntityOverseaPayMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayMerchant from a JSON string
unibee_internal_model_entity_oversea_pay_merchant_instance = UnibeeInternalModelEntityOverseaPayMerchant.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayMerchant.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_merchant_dict = unibee_internal_model_entity_oversea_pay_merchant_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayMerchant from a dict
unibee_internal_model_entity_oversea_pay_merchant_form_dict = unibee_internal_model_entity_oversea_pay_merchant.from_dict(unibee_internal_model_entity_oversea_pay_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


