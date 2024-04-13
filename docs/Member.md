# openapi_client.Member

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**member_list_get**](Member.md#member_list_get) | **GET** /merchant/member/list | Get Merchant Member List
[**member_logout_post**](Member.md#member_logout_post) | **POST** /merchant/member/logout | Merchant Member Logout
[**member_new_member_post**](Member.md#member_new_member_post) | **POST** /merchant/member/new_member | Invite member
[**member_password_reset_post**](Member.md#member_password_reset_post) | **POST** /merchant/member/passwordReset | Merchant Member Reset Password
[**member_profile_get**](Member.md#member_profile_get) | **GET** /merchant/member/profile | Get Merchant Member Profile
[**member_update_member_role_post**](Member.md#member_update_member_role_post) | **POST** /merchant/member/update_member_role | Update Member Role


# **member_list_get**
> MerchantMemberListGet200Response member_list_get()

Get Merchant Member List

### Example


```python
import openapi_client
from openapi_client.models.merchant_member_list_get200_response import MerchantMemberListGet200Response
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
    api_instance = openapi_client.Member(api_client)

    try:
        # Get Merchant Member List
        api_response = api_instance.member_list_get()
        print("The response of Member->member_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantMemberListGet200Response**](MerchantMemberListGet200Response.md)

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

# **member_logout_post**
> MerchantAuthSsoLoginOTPPost200Response member_logout_post(body)

Merchant Member Logout

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
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
    api_instance = openapi_client.Member(api_client)
    body = None # object | 

    try:
        # Merchant Member Logout
        api_response = api_instance.member_logout_post(body)
        print("The response of Member->member_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_logout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **member_new_member_post**
> MerchantAuthSsoLoginOTPPost200Response member_new_member_post(unibee_api_merchant_member_new_member_req)

Invite member

Will send email to member email provided, member can enter admin portal by email otp login

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_member_new_member_req import UnibeeApiMerchantMemberNewMemberReq
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
    api_instance = openapi_client.Member(api_client)
    unibee_api_merchant_member_new_member_req = openapi_client.UnibeeApiMerchantMemberNewMemberReq() # UnibeeApiMerchantMemberNewMemberReq | 

    try:
        # Invite member
        api_response = api_instance.member_new_member_post(unibee_api_merchant_member_new_member_req)
        print("The response of Member->member_new_member_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_new_member_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_member_new_member_req** | [**UnibeeApiMerchantMemberNewMemberReq**](UnibeeApiMerchantMemberNewMemberReq.md)|  | 

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

# **member_password_reset_post**
> MerchantAuthSsoLoginOTPPost200Response member_password_reset_post(unibee_api_merchant_member_password_reset_req)

Merchant Member Reset Password

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_member_password_reset_req import UnibeeApiMerchantMemberPasswordResetReq
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
    api_instance = openapi_client.Member(api_client)
    unibee_api_merchant_member_password_reset_req = openapi_client.UnibeeApiMerchantMemberPasswordResetReq() # UnibeeApiMerchantMemberPasswordResetReq | 

    try:
        # Merchant Member Reset Password
        api_response = api_instance.member_password_reset_post(unibee_api_merchant_member_password_reset_req)
        print("The response of Member->member_password_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_password_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_member_password_reset_req** | [**UnibeeApiMerchantMemberPasswordResetReq**](UnibeeApiMerchantMemberPasswordResetReq.md)|  | 

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

# **member_profile_get**
> MerchantAuthSsoRegisterVerifyPost200Response member_profile_get()

Get Merchant Member Profile

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_register_verify_post200_response import MerchantAuthSsoRegisterVerifyPost200Response
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
    api_instance = openapi_client.Member(api_client)

    try:
        # Get Merchant Member Profile
        api_response = api_instance.member_profile_get()
        print("The response of Member->member_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_profile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantAuthSsoRegisterVerifyPost200Response**](MerchantAuthSsoRegisterVerifyPost200Response.md)

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

# **member_update_member_role_post**
> MerchantAuthSsoLoginOTPPost200Response member_update_member_role_post(unibee_api_merchant_member_update_member_role_req)

Update Member Role

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_member_update_member_role_req import UnibeeApiMerchantMemberUpdateMemberRoleReq
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
    api_instance = openapi_client.Member(api_client)
    unibee_api_merchant_member_update_member_role_req = openapi_client.UnibeeApiMerchantMemberUpdateMemberRoleReq() # UnibeeApiMerchantMemberUpdateMemberRoleReq | 

    try:
        # Update Member Role
        api_response = api_instance.member_update_member_role_post(unibee_api_merchant_member_update_member_role_req)
        print("The response of Member->member_update_member_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Member->member_update_member_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_member_update_member_role_req** | [**UnibeeApiMerchantMemberUpdateMemberRoleReq**](UnibeeApiMerchantMemberUpdateMemberRoleReq.md)|  | 

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

