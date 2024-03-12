# UnibeeApiBeanMerchantSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | [optional] 
**business_num** | **str** | business_num | [optional] 
**company_logo** | **str** | company_logo | [optional] 
**company_name** | **str** | company_name | [optional] 
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | email | [optional] 
**home_url** | **str** |  | [optional] 
**host** | **str** | merchant user portal host | [optional] 
**id** | **int** | merchant_id | [optional] 
**idcard** | **str** | idcard | [optional] 
**location** | **str** | location | [optional] 
**name** | **str** | name | [optional] 
**phone** | **str** | phone | [optional] 
**time_zone** | **str** | merchant default time zone | [optional] 
**type** | **int** | type | [optional] 
**user_id** | **int** | create_user_id | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_simplify import UnibeeApiBeanMerchantSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantSimplify from a JSON string
unibee_api_bean_merchant_simplify_instance = UnibeeApiBeanMerchantSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_simplify_dict = unibee_api_bean_merchant_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantSimplify from a dict
unibee_api_bean_merchant_simplify_form_dict = unibee_api_bean_merchant_simplify.from_dict(unibee_api_bean_merchant_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


