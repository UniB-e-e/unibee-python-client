# openapi_client.Profile

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get**](Profile.md#get_get) | **GET** /merchant/get | Get Merchant Info
[**update_post**](Profile.md#update_post) | **POST** /merchant/update | Update Merchant Info


# **get_get**
> MerchantGetGet200Response get_get()

Get Merchant Info

### Example


```python
import openapi_client
from openapi_client.models.merchant_get_get200_response import MerchantGetGet200Response
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
    api_instance = openapi_client.Profile(api_client)

    try:
        # Get Merchant Info
        api_response = api_instance.get_get()
        print("The response of Profile->get_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->get_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantGetGet200Response**](MerchantGetGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post**
> MerchantGetGet200Response update_post(unibee_api_merchant_profile_update_req)

Update Merchant Info

### Example


```python
import openapi_client
from openapi_client.models.merchant_get_get200_response import MerchantGetGet200Response
from openapi_client.models.unibee_api_merchant_profile_update_req import UnibeeApiMerchantProfileUpdateReq
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
    api_instance = openapi_client.Profile(api_client)
    unibee_api_merchant_profile_update_req = openapi_client.UnibeeApiMerchantProfileUpdateReq() # UnibeeApiMerchantProfileUpdateReq | 

    try:
        # Update Merchant Info
        api_response = api_instance.update_post(unibee_api_merchant_profile_update_req)
        print("The response of Profile->update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_profile_update_req** | [**UnibeeApiMerchantProfileUpdateReq**](UnibeeApiMerchantProfileUpdateReq.md)|  | 

### Return type

[**MerchantGetGet200Response**](MerchantGetGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

