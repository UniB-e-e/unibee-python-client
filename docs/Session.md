# openapi_client.Session

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_new_session_post**](Session.md#session_new_session_post) | **POST** /merchant/session/new_session | New User Portal Session


# **session_new_session_post**
> MerchantSessionNewSessionPost200Response session_new_session_post(unibee_api_merchant_session_new_req)

New User Portal Session

### Example


```python
import openapi_client
from openapi_client.models.merchant_session_new_session_post200_response import MerchantSessionNewSessionPost200Response
from openapi_client.models.unibee_api_merchant_session_new_req import UnibeeApiMerchantSessionNewReq
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
    api_instance = openapi_client.Session(api_client)
    unibee_api_merchant_session_new_req = openapi_client.UnibeeApiMerchantSessionNewReq() # UnibeeApiMerchantSessionNewReq | 

    try:
        # New User Portal Session
        api_response = api_instance.session_new_session_post(unibee_api_merchant_session_new_req)
        print("The response of Session->session_new_session_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Session->session_new_session_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_session_new_req** | [**UnibeeApiMerchantSessionNewReq**](UnibeeApiMerchantSessionNewReq.md)|  | 

### Return type

[**MerchantSessionNewSessionPost200Response**](MerchantSessionNewSessionPost200Response.md)

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

