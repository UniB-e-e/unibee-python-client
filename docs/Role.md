# openapi_client.Role

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_delete_post**](Role.md#role_delete_post) | **POST** /merchant/role/delete | Delete Merchant Role
[**role_edit_post**](Role.md#role_edit_post) | **POST** /merchant/role/edit | Edit Merchant Role
[**role_list_get**](Role.md#role_list_get) | **GET** /merchant/role/list | Get Merchant Role List
[**role_new_post**](Role.md#role_new_post) | **POST** /merchant/role/new | New Merchant Role


# **role_delete_post**
> MerchantAuthSsoLoginOTPPost200Response role_delete_post(unibee_api_merchant_role_delete_req)

Delete Merchant Role

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_role_delete_req import UnibeeApiMerchantRoleDeleteReq
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
    api_instance = openapi_client.Role(api_client)
    unibee_api_merchant_role_delete_req = openapi_client.UnibeeApiMerchantRoleDeleteReq() # UnibeeApiMerchantRoleDeleteReq | 

    try:
        # Delete Merchant Role
        api_response = api_instance.role_delete_post(unibee_api_merchant_role_delete_req)
        print("The response of Role->role_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Role->role_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_role_delete_req** | [**UnibeeApiMerchantRoleDeleteReq**](UnibeeApiMerchantRoleDeleteReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

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

# **role_edit_post**
> MerchantAuthSsoLoginOTPPost200Response role_edit_post(unibee_api_merchant_role_edit_req)

Edit Merchant Role

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_role_edit_req import UnibeeApiMerchantRoleEditReq
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
    api_instance = openapi_client.Role(api_client)
    unibee_api_merchant_role_edit_req = openapi_client.UnibeeApiMerchantRoleEditReq() # UnibeeApiMerchantRoleEditReq | 

    try:
        # Edit Merchant Role
        api_response = api_instance.role_edit_post(unibee_api_merchant_role_edit_req)
        print("The response of Role->role_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Role->role_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_role_edit_req** | [**UnibeeApiMerchantRoleEditReq**](UnibeeApiMerchantRoleEditReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

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

# **role_list_get**
> MerchantRoleListGet200Response role_list_get()

Get Merchant Role List

### Example


```python
import openapi_client
from openapi_client.models.merchant_role_list_get200_response import MerchantRoleListGet200Response
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
    api_instance = openapi_client.Role(api_client)

    try:
        # Get Merchant Role List
        api_response = api_instance.role_list_get()
        print("The response of Role->role_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Role->role_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantRoleListGet200Response**](MerchantRoleListGet200Response.md)

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

# **role_new_post**
> MerchantAuthSsoLoginOTPPost200Response role_new_post(unibee_api_merchant_role_new_req)

New Merchant Role

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_role_new_req import UnibeeApiMerchantRoleNewReq
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
    api_instance = openapi_client.Role(api_client)
    unibee_api_merchant_role_new_req = openapi_client.UnibeeApiMerchantRoleNewReq() # UnibeeApiMerchantRoleNewReq | 

    try:
        # New Merchant Role
        api_response = api_instance.role_new_post(unibee_api_merchant_role_new_req)
        print("The response of Role->role_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Role->role_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_role_new_req** | [**UnibeeApiMerchantRoleNewReq**](UnibeeApiMerchantRoleNewReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

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

