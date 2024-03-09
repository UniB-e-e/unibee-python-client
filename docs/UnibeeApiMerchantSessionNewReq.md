# UnibeeApiMerchantSessionNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address | [optional] 
**email** | **str** | Email | 
**external_user_id** | **str** | ExternalUserId | 
**first_name** | **str** | First Name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**password** | **str** | Password | [optional] 
**phone** | **str** | Phone | [optional] 
**return_url** | **str** | ReturnUrl | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_session_new_req import UnibeeApiMerchantSessionNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSessionNewReq from a JSON string
unibee_api_merchant_session_new_req_instance = UnibeeApiMerchantSessionNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSessionNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_session_new_req_dict = unibee_api_merchant_session_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSessionNewReq from a dict
unibee_api_merchant_session_new_req_form_dict = unibee_api_merchant_session_new_req.from_dict(unibee_api_merchant_session_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


