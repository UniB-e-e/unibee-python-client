# UnibeeApiMerchantUserUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_in** | **str** | LinkedIn | [optional] 
**address** | **str** | Billing Address | 
**company_name** | **str** | Company Name | [optional] 
**country_code** | **str** | Country Code | 
**country_name** | **str** | Country Name | 
**email** | **str** | Email | 
**facebook** | **str** | Facebook | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last Name | 
**other_social_info** | **str** | Other Social Info | [optional] 
**payment_method** | **str** | Payment Method | [optional] 
**phone** | **str** | Phone | [optional] 
**telegram** | **str** | Telegram | [optional] 
**tiktok** | **str** | Tiktok | [optional] 
**user_id** | **int** | User Id | 
**v_at_number** | **str** | VAT Number | [optional] 
**we_chat** | **str** | WeChat | [optional] 
**whats_app** | **str** | WhatsApp | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_user_update_req import UnibeeApiMerchantUserUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantUserUpdateReq from a JSON string
unibee_api_merchant_user_update_req_instance = UnibeeApiMerchantUserUpdateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantUserUpdateReq.to_json()

# convert the object into a dict
unibee_api_merchant_user_update_req_dict = unibee_api_merchant_user_update_req_instance.to_dict()
# create an instance of UnibeeApiMerchantUserUpdateReq from a dict
unibee_api_merchant_user_update_req_form_dict = unibee_api_merchant_user_update_req.from_dict(unibee_api_merchant_user_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


