# UnibeeApiMerchantSessionNewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_session** | **str** | ClientSession | [optional] 
**client_token** | **str** | ClientToken | [optional] 
**email** | **str** | Email | [optional] 
**external_user_id** | **str** | ExternalUserId | [optional] 
**url** | **str** | Url | [optional] 
**user_id** | **str** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_session_new_res import UnibeeApiMerchantSessionNewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSessionNewRes from a JSON string
unibee_api_merchant_session_new_res_instance = UnibeeApiMerchantSessionNewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSessionNewRes.to_json()

# convert the object into a dict
unibee_api_merchant_session_new_res_dict = unibee_api_merchant_session_new_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSessionNewRes from a dict
unibee_api_merchant_session_new_res_form_dict = unibee_api_merchant_session_new_res.from_dict(unibee_api_merchant_session_new_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


