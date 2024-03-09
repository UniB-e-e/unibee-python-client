# openapi_client.Auth

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_sso_login_otp_post**](Auth.md#auth_sso_login_otp_post) | **POST** /merchant/auth/sso/loginOTP | Login OTP
[**auth_sso_login_otp_verify_post**](Auth.md#auth_sso_login_otp_verify_post) | **POST** /merchant/auth/sso/loginOTPVerify | Merchant User OTP Login Verify
[**auth_sso_login_post**](Auth.md#auth_sso_login_post) | **POST** /merchant/auth/sso/login | Login
[**auth_sso_password_forget_otp_post**](Auth.md#auth_sso_password_forget_otp_post) | **POST** /merchant/auth/sso/passwordForgetOTP | Merchant Password Forget OTP
[**auth_sso_password_forget_otp_verify_post**](Auth.md#auth_sso_password_forget_otp_verify_post) | **POST** /merchant/auth/sso/passwordForgetOTPVerify | Merchant Password Forget OTP Verify
[**auth_sso_register_post**](Auth.md#auth_sso_register_post) | **POST** /merchant/auth/sso/register | Merchant Register
[**auth_sso_register_verify_post**](Auth.md#auth_sso_register_verify_post) | **POST** /merchant/auth/sso/registerVerify | Merchant Register Verify


# **auth_sso_login_otp_post**
> MerchantAuthSsoLoginOTPPost200Response auth_sso_login_otp_post(unibee_api_merchant_auth_login_otp_req)

Login OTP

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_auth_login_otp_req import UnibeeApiMerchantAuthLoginOtpReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_login_otp_req = openapi_client.UnibeeApiMerchantAuthLoginOtpReq() # UnibeeApiMerchantAuthLoginOtpReq | 

    try:
        # Login OTP
        api_response = api_instance.auth_sso_login_otp_post(unibee_api_merchant_auth_login_otp_req)
        print("The response of Auth->auth_sso_login_otp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_login_otp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_login_otp_req** | [**UnibeeApiMerchantAuthLoginOtpReq**](UnibeeApiMerchantAuthLoginOtpReq.md)|  | 

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

# **auth_sso_login_otp_verify_post**
> MerchantAuthSsoLoginPost200Response auth_sso_login_otp_verify_post(unibee_api_merchant_auth_login_otp_verify_req)

Merchant User OTP Login Verify

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_post200_response import MerchantAuthSsoLoginPost200Response
from openapi_client.models.unibee_api_merchant_auth_login_otp_verify_req import UnibeeApiMerchantAuthLoginOtpVerifyReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_login_otp_verify_req = openapi_client.UnibeeApiMerchantAuthLoginOtpVerifyReq() # UnibeeApiMerchantAuthLoginOtpVerifyReq | 

    try:
        # Merchant User OTP Login Verify
        api_response = api_instance.auth_sso_login_otp_verify_post(unibee_api_merchant_auth_login_otp_verify_req)
        print("The response of Auth->auth_sso_login_otp_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_login_otp_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_login_otp_verify_req** | [**UnibeeApiMerchantAuthLoginOtpVerifyReq**](UnibeeApiMerchantAuthLoginOtpVerifyReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginPost200Response**](MerchantAuthSsoLoginPost200Response.md)

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

# **auth_sso_login_post**
> MerchantAuthSsoLoginPost200Response auth_sso_login_post(unibee_api_merchant_auth_login_req)

Login

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_post200_response import MerchantAuthSsoLoginPost200Response
from openapi_client.models.unibee_api_merchant_auth_login_req import UnibeeApiMerchantAuthLoginReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_login_req = openapi_client.UnibeeApiMerchantAuthLoginReq() # UnibeeApiMerchantAuthLoginReq | 

    try:
        # Login
        api_response = api_instance.auth_sso_login_post(unibee_api_merchant_auth_login_req)
        print("The response of Auth->auth_sso_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_login_req** | [**UnibeeApiMerchantAuthLoginReq**](UnibeeApiMerchantAuthLoginReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginPost200Response**](MerchantAuthSsoLoginPost200Response.md)

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

# **auth_sso_password_forget_otp_post**
> MerchantAuthSsoLoginOTPPost200Response auth_sso_password_forget_otp_post(unibee_api_merchant_auth_password_forget_otp_req)

Merchant Password Forget OTP

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_auth_password_forget_otp_req import UnibeeApiMerchantAuthPasswordForgetOtpReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_password_forget_otp_req = openapi_client.UnibeeApiMerchantAuthPasswordForgetOtpReq() # UnibeeApiMerchantAuthPasswordForgetOtpReq | 

    try:
        # Merchant Password Forget OTP
        api_response = api_instance.auth_sso_password_forget_otp_post(unibee_api_merchant_auth_password_forget_otp_req)
        print("The response of Auth->auth_sso_password_forget_otp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_password_forget_otp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_password_forget_otp_req** | [**UnibeeApiMerchantAuthPasswordForgetOtpReq**](UnibeeApiMerchantAuthPasswordForgetOtpReq.md)|  | 

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

# **auth_sso_password_forget_otp_verify_post**
> MerchantAuthSsoLoginOTPPost200Response auth_sso_password_forget_otp_verify_post(unibee_api_merchant_auth_password_forget_otp_verify_req)

Merchant Password Forget OTP Verify

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_auth_password_forget_otp_verify_req import UnibeeApiMerchantAuthPasswordForgetOtpVerifyReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_password_forget_otp_verify_req = openapi_client.UnibeeApiMerchantAuthPasswordForgetOtpVerifyReq() # UnibeeApiMerchantAuthPasswordForgetOtpVerifyReq | 

    try:
        # Merchant Password Forget OTP Verify
        api_response = api_instance.auth_sso_password_forget_otp_verify_post(unibee_api_merchant_auth_password_forget_otp_verify_req)
        print("The response of Auth->auth_sso_password_forget_otp_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_password_forget_otp_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_password_forget_otp_verify_req** | [**UnibeeApiMerchantAuthPasswordForgetOtpVerifyReq**](UnibeeApiMerchantAuthPasswordForgetOtpVerifyReq.md)|  | 

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

# **auth_sso_register_post**
> MerchantAuthSsoLoginOTPPost200Response auth_sso_register_post(unibee_api_merchant_auth_register_req)

Merchant Register

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_auth_register_req import UnibeeApiMerchantAuthRegisterReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_register_req = openapi_client.UnibeeApiMerchantAuthRegisterReq() # UnibeeApiMerchantAuthRegisterReq | 

    try:
        # Merchant Register
        api_response = api_instance.auth_sso_register_post(unibee_api_merchant_auth_register_req)
        print("The response of Auth->auth_sso_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_register_req** | [**UnibeeApiMerchantAuthRegisterReq**](UnibeeApiMerchantAuthRegisterReq.md)|  | 

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

# **auth_sso_register_verify_post**
> MerchantAuthSsoRegisterVerifyPost200Response auth_sso_register_verify_post(unibee_api_merchant_auth_register_verify_req)

Merchant Register Verify

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_register_verify_post200_response import MerchantAuthSsoRegisterVerifyPost200Response
from openapi_client.models.unibee_api_merchant_auth_register_verify_req import UnibeeApiMerchantAuthRegisterVerifyReq
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
    api_instance = openapi_client.Auth(api_client)
    unibee_api_merchant_auth_register_verify_req = openapi_client.UnibeeApiMerchantAuthRegisterVerifyReq() # UnibeeApiMerchantAuthRegisterVerifyReq | 

    try:
        # Merchant Register Verify
        api_response = api_instance.auth_sso_register_verify_post(unibee_api_merchant_auth_register_verify_req)
        print("The response of Auth->auth_sso_register_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Auth->auth_sso_register_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_auth_register_verify_req** | [**UnibeeApiMerchantAuthRegisterVerifyReq**](UnibeeApiMerchantAuthRegisterVerifyReq.md)|  | 

### Return type

[**MerchantAuthSsoRegisterVerifyPost200Response**](MerchantAuthSsoRegisterVerifyPost200Response.md)

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

