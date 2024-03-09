# UnibeeApiMerchantProfileUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | address | [optional] 
**company_logo** | **str** | company_logo | [optional] 
**company_name** | **str** | company_name | [optional] 
**email** | **str** | email | [optional] 
**host** | **str** | User Portal Host | [optional] 
**phone** | **str** | phone | [optional] 
**time_zone** | **str** | User TimeZone | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_profile_update_req import UnibeeApiMerchantProfileUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantProfileUpdateReq from a JSON string
unibee_api_merchant_profile_update_req_instance = UnibeeApiMerchantProfileUpdateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantProfileUpdateReq.to_json()

# convert the object into a dict
unibee_api_merchant_profile_update_req_dict = unibee_api_merchant_profile_update_req_instance.to_dict()
# create an instance of UnibeeApiMerchantProfileUpdateReq from a dict
unibee_api_merchant_profile_update_req_form_dict = unibee_api_merchant_profile_update_req.from_dict(unibee_api_merchant_profile_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


