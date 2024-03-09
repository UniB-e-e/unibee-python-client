# openapi_client.User

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_frozen_user_post**](User.md#user_frozen_user_post) | **POST** /merchant/user/frozen_user | Merchant Frozen User
[**user_get_get**](User.md#user_get_get) | **GET** /merchant/user/get | Get User Profile
[**user_list_get**](User.md#user_list_get) | **GET** /merchant/user/list | User List
[**user_list_post**](User.md#user_list_post) | **POST** /merchant/user/list | User List
[**user_release_user_post**](User.md#user_release_user_post) | **POST** /merchant/user/release_user | Merchant Release User
[**user_search_get**](User.md#user_search_get) | **GET** /merchant/user/search | User Search
[**user_search_post**](User.md#user_search_post) | **POST** /merchant/user/search | User Search
[**user_update_post**](User.md#user_update_post) | **POST** /merchant/user/update | Update User Profile


# **user_frozen_user_post**
> MerchantAuthSsoLoginOTPPost200Response user_frozen_user_post(unibee_api_merchant_user_frozen_req)

Merchant Frozen User

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_user_frozen_req import UnibeeApiMerchantUserFrozenReq
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
    api_instance = openapi_client.User(api_client)
    unibee_api_merchant_user_frozen_req = openapi_client.UnibeeApiMerchantUserFrozenReq() # UnibeeApiMerchantUserFrozenReq | 

    try:
        # Merchant Frozen User
        api_response = api_instance.user_frozen_user_post(unibee_api_merchant_user_frozen_req)
        print("The response of User->user_frozen_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_frozen_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_user_frozen_req** | [**UnibeeApiMerchantUserFrozenReq**](UnibeeApiMerchantUserFrozenReq.md)|  | 

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

# **user_get_get**
> MerchantUserGetGet200Response user_get_get(user_id=user_id)

Get User Profile

### Example


```python
import openapi_client
from openapi_client.models.merchant_user_get_get200_response import MerchantUserGetGet200Response
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
    api_instance = openapi_client.User(api_client)
    user_id = 56 # int | UserId (optional)

    try:
        # Get User Profile
        api_response = api_instance.user_get_get(user_id=user_id)
        print("The response of User->user_get_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_get_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| UserId | [optional] 

### Return type

[**MerchantUserGetGet200Response**](MerchantUserGetGet200Response.md)

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

# **user_list_get**
> MerchantUserListGet200Response user_list_get(user_id=user_id, first_name=first_name, last_name=last_name, email=email, status=status, delete_include=delete_include, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

User List

### Example


```python
import openapi_client
from openapi_client.models.merchant_user_list_get200_response import MerchantUserListGet200Response
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
    api_instance = openapi_client.User(api_client)
    user_id = 56 # int | Filter UserId (optional)
    first_name = 'first_name_example' # str | Search FirstName (optional)
    last_name = 'last_name_example' # str | Search LastName (optional)
    email = 'email_example' # str | Search Filter Email (optional)
    status = [56] # List[int] | Status, 0-Active｜2-Frozen (optional)
    delete_include = True # bool | Deleted Involved，Need Admin (optional)
    sort_field = 'sort_field_example' # str | Sort，user_id|gmt_create|email|user_name|subscription_name|subscription_status|payment_method|recurring_amount|billing_type，Default gmt_create (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page,Start 0 (optional)
    count = 56 # int | Count OF Page (optional)

    try:
        # User List
        api_response = api_instance.user_list_get(user_id=user_id, first_name=first_name, last_name=last_name, email=email, status=status, delete_include=delete_include, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of User->user_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Filter UserId | [optional] 
 **first_name** | **str**| Search FirstName | [optional] 
 **last_name** | **str**| Search LastName | [optional] 
 **email** | **str**| Search Filter Email | [optional] 
 **status** | [**List[int]**](int.md)| Status, 0-Active｜2-Frozen | [optional] 
 **delete_include** | **bool**| Deleted Involved，Need Admin | [optional] 
 **sort_field** | **str**| Sort，user_id|gmt_create|email|user_name|subscription_name|subscription_status|payment_method|recurring_amount|billing_type，Default gmt_create | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page,Start 0 | [optional] 
 **count** | **int**| Count OF Page | [optional] 

### Return type

[**MerchantUserListGet200Response**](MerchantUserListGet200Response.md)

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

# **user_list_post**
> MerchantUserListGet200Response user_list_post(unibee_api_merchant_user_list_req)

User List

### Example


```python
import openapi_client
from openapi_client.models.merchant_user_list_get200_response import MerchantUserListGet200Response
from openapi_client.models.unibee_api_merchant_user_list_req import UnibeeApiMerchantUserListReq
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
    api_instance = openapi_client.User(api_client)
    unibee_api_merchant_user_list_req = openapi_client.UnibeeApiMerchantUserListReq() # UnibeeApiMerchantUserListReq | 

    try:
        # User List
        api_response = api_instance.user_list_post(unibee_api_merchant_user_list_req)
        print("The response of User->user_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_user_list_req** | [**UnibeeApiMerchantUserListReq**](UnibeeApiMerchantUserListReq.md)|  | 

### Return type

[**MerchantUserListGet200Response**](MerchantUserListGet200Response.md)

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

# **user_release_user_post**
> MerchantAuthSsoLoginOTPPost200Response user_release_user_post(unibee_api_merchant_user_release_req)

Merchant Release User

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_user_release_req import UnibeeApiMerchantUserReleaseReq
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
    api_instance = openapi_client.User(api_client)
    unibee_api_merchant_user_release_req = openapi_client.UnibeeApiMerchantUserReleaseReq() # UnibeeApiMerchantUserReleaseReq | 

    try:
        # Merchant Release User
        api_response = api_instance.user_release_user_post(unibee_api_merchant_user_release_req)
        print("The response of User->user_release_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_release_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_user_release_req** | [**UnibeeApiMerchantUserReleaseReq**](UnibeeApiMerchantUserReleaseReq.md)|  | 

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

# **user_search_get**
> MerchantUserListGet200Response user_search_get(search_key=search_key)

User Search

### Example


```python
import openapi_client
from openapi_client.models.merchant_user_list_get200_response import MerchantUserListGet200Response
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
    api_instance = openapi_client.User(api_client)
    search_key = 'search_key_example' # str | SearchKey, Will Search UserId|Email|UserName|CompanyName|SubscriptionId|VatNumber|InvoiceId||PaymentId (optional)

    try:
        # User Search
        api_response = api_instance.user_search_get(search_key=search_key)
        print("The response of User->user_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**| SearchKey, Will Search UserId|Email|UserName|CompanyName|SubscriptionId|VatNumber|InvoiceId||PaymentId | [optional] 

### Return type

[**MerchantUserListGet200Response**](MerchantUserListGet200Response.md)

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

# **user_search_post**
> MerchantUserListGet200Response user_search_post(unibee_api_merchant_user_search_req)

User Search

### Example


```python
import openapi_client
from openapi_client.models.merchant_user_list_get200_response import MerchantUserListGet200Response
from openapi_client.models.unibee_api_merchant_user_search_req import UnibeeApiMerchantUserSearchReq
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
    api_instance = openapi_client.User(api_client)
    unibee_api_merchant_user_search_req = openapi_client.UnibeeApiMerchantUserSearchReq() # UnibeeApiMerchantUserSearchReq | 

    try:
        # User Search
        api_response = api_instance.user_search_post(unibee_api_merchant_user_search_req)
        print("The response of User->user_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_user_search_req** | [**UnibeeApiMerchantUserSearchReq**](UnibeeApiMerchantUserSearchReq.md)|  | 

### Return type

[**MerchantUserListGet200Response**](MerchantUserListGet200Response.md)

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

# **user_update_post**
> MerchantAuthSsoLoginOTPPost200Response user_update_post(unibee_api_merchant_user_update_req)

Update User Profile

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_user_update_req import UnibeeApiMerchantUserUpdateReq
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
    api_instance = openapi_client.User(api_client)
    unibee_api_merchant_user_update_req = openapi_client.UnibeeApiMerchantUserUpdateReq() # UnibeeApiMerchantUserUpdateReq | 

    try:
        # Update User Profile
        api_response = api_instance.user_update_post(unibee_api_merchant_user_update_req)
        print("The response of User->user_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling User->user_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_user_update_req** | [**UnibeeApiMerchantUserUpdateReq**](UnibeeApiMerchantUserUpdateReq.md)|  | 

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

