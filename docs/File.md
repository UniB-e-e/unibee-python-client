# openapi_client.File

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oss_file_post**](File.md#oss_file_post) | **POST** /merchant/oss/file | Upload File


# **oss_file_post**
> MerchantOssFilePost200Response oss_file_post(file=file)

Upload File

### Example


```python
import openapi_client
from openapi_client.models.merchant_oss_file_post200_response import MerchantOssFilePost200Response
from openapi_client.models.bytearray import bytearray
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.File(api_client)
    file = None # bytearray | File To Upload (optional)

    try:
        # Upload File
        api_response = api_instance.oss_file_post(file=file)
        print("The response of File->oss_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling File->oss_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**bytearray**](bytearray.md)| File To Upload | [optional] 

### Return type

[**MerchantOssFilePost200Response**](MerchantOssFilePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

