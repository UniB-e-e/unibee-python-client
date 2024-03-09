# MerchantSessionNewSessionPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_token** | **str** | ClientToken | [optional] 
**email** | **str** | Email | [optional] 
**external_user_id** | **str** | ExternalUserId | [optional] 
**url** | **str** | Url | [optional] 
**user_id** | **str** | UserId | [optional] 

## Example

```python
from openapi_client.models.merchant_session_new_session_post200_response_data import MerchantSessionNewSessionPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSessionNewSessionPost200ResponseData from a JSON string
merchant_session_new_session_post200_response_data_instance = MerchantSessionNewSessionPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSessionNewSessionPost200ResponseData.to_json()

# convert the object into a dict
merchant_session_new_session_post200_response_data_dict = merchant_session_new_session_post200_response_data_instance.to_dict()
# create an instance of MerchantSessionNewSessionPost200ResponseData from a dict
merchant_session_new_session_post200_response_data_form_dict = merchant_session_new_session_post200_response_data.from_dict(merchant_session_new_session_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


