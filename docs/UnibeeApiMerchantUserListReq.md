# UnibeeApiMerchantUserListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count OF Page | [optional] 
**delete_include** | **bool** | Deleted Involved，Need Admin | [optional] 
**email** | **str** | Search Filter Email | [optional] 
**first_name** | **str** | Search FirstName | [optional] 
**last_name** | **str** | Search LastName | [optional] 
**page** | **int** | Page,Start 0 | [optional] 
**sort_field** | **str** | Sort，user_id|gmt_create|email|user_name|subscription_name|subscription_status|payment_method|recurring_amount|billing_type，Default gmt_create | [optional] 
**sort_type** | **str** | Sort Type，asc|desc，Default desc | [optional] 
**status** | **List[int]** | Status, 0-Active｜2-Frozen | [optional] 
**user_id** | **int** | Filter UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_user_list_req import UnibeeApiMerchantUserListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantUserListReq from a JSON string
unibee_api_merchant_user_list_req_instance = UnibeeApiMerchantUserListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantUserListReq.to_json()

# convert the object into a dict
unibee_api_merchant_user_list_req_dict = unibee_api_merchant_user_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantUserListReq from a dict
unibee_api_merchant_user_list_req_form_dict = unibee_api_merchant_user_list_req.from_dict(unibee_api_merchant_user_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


