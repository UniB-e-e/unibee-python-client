# UnibeeApiBeanUserAccountSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | [optional] 
**avatar_url** | **str** | avator url | [optional] 
**billing_type** | **int** | 1-recurring,2-one-time | [optional] 
**birthday** | **str** | brithday | [optional] 
**company_name** | **str** | company name | [optional] 
**country_code** | **str** | country_code | [optional] 
**country_name** | **str** | country_name | [optional] 
**create_time** | **int** | create utc time | [optional] 
**custom** | **str** | custom | [optional] 
**email** | **str** | email | [optional] 
**external_user_id** | **str** | external_user_id | [optional] 
**facebook** | **str** | facebook | [optional] 
**first_name** | **str** | first name | [optional] 
**gateway_id** | **str** | gateway_id | [optional] 
**gender** | **str** | gender | [optional] 
**id** | **int** | userId | [optional] 
**is_risk** | **int** | is risk account (deperated) | [optional] 
**is_special** | **int** | is special account（0.no，1.yes）- deperated | [optional] 
**last_login_at** | **int** | last login time, utc time | [optional] 
**last_name** | **str** | last name | [optional] 
**linked_in** | **str** | linkedin | [optional] 
**merchant_id** | **int** | merchant_id | [optional] 
**mobile** | **str** | mobile | [optional] 
**other_social_info** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**phone** | **str** | phone | [optional] 
**profession** | **str** | profession | [optional] 
**re_mark** | **str** | note | [optional] 
**recurring_amount** | **int** | total recurring amount, cent | [optional] 
**school** | **str** | school | [optional] 
**status** | **int** | 0-Active, 2-Frozen | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**subscription_name** | **str** | subscription name | [optional] 
**subscription_status** | **int** | sub status，0-Init | 1-Create｜2-Active｜3-PendingInActive | 4-Cancel | 5-Expire | 6- Suspend| 7-Incomplete | [optional] 
**telegram** | **str** | telegram | [optional] 
**tik_tok** | **str** | tictok | [optional] 
**time_zone** | **str** |  | [optional] 
**user_name** | **str** | user name | [optional] 
**v_at_number** | **str** | vat number | [optional] 
**version** | **int** | version | [optional] 
**we_chat** | **str** | wechat | [optional] 
**whats_app** | **str** | whats app | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_user_account_simplify import UnibeeApiBeanUserAccountSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanUserAccountSimplify from a JSON string
unibee_api_bean_user_account_simplify_instance = UnibeeApiBeanUserAccountSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanUserAccountSimplify.to_json()

# convert the object into a dict
unibee_api_bean_user_account_simplify_dict = unibee_api_bean_user_account_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanUserAccountSimplify from a dict
unibee_api_bean_user_account_simplify_form_dict = unibee_api_bean_user_account_simplify.from_dict(unibee_api_bean_user_account_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


