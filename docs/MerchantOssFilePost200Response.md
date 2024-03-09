# MerchantOssFilePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**data** | [**MerchantOssFilePost200ResponseData**](MerchantOssFilePost200ResponseData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**redirect** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_oss_file_post200_response import MerchantOssFilePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantOssFilePost200Response from a JSON string
merchant_oss_file_post200_response_instance = MerchantOssFilePost200Response.from_json(json)
# print the JSON string representation of the object
print MerchantOssFilePost200Response.to_json()

# convert the object into a dict
merchant_oss_file_post200_response_dict = merchant_oss_file_post200_response_instance.to_dict()
# create an instance of MerchantOssFilePost200Response from a dict
merchant_oss_file_post200_response_form_dict = merchant_oss_file_post200_response.from_dict(merchant_oss_file_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


