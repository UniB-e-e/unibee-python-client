# openapi_client.SubscriptionNote

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_admin_note_list_get**](SubscriptionNote.md#subscription_admin_note_list_get) | **GET** /merchant/subscription/admin_note_list | Merchant Subscription Note List
[**subscription_admin_note_list_post**](SubscriptionNote.md#subscription_admin_note_list_post) | **POST** /merchant/subscription/admin_note_list | Merchant Subscription Note List
[**subscription_new_admin_note_post**](SubscriptionNote.md#subscription_new_admin_note_post) | **POST** /merchant/subscription/new_admin_note | Merchant New Subscription Note


# **subscription_admin_note_list_get**
> MerchantSubscriptionAdminNoteListGet200Response subscription_admin_note_list_get(subscription_id, page=page, count=count)

Merchant Subscription Note List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_admin_note_list_get200_response import MerchantSubscriptionAdminNoteListGet200Response
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
    api_instance = openapi_client.SubscriptionNote(api_client)
    subscription_id = 'subscription_id_example' # str | SubscriptionId
    page = 56 # int | Page, Start WIth 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Merchant Subscription Note List
        api_response = api_instance.subscription_admin_note_list_get(subscription_id, page=page, count=count)
        print("The response of SubscriptionNote->subscription_admin_note_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionNote->subscription_admin_note_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| SubscriptionId | 
 **page** | **int**| Page, Start WIth 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantSubscriptionAdminNoteListGet200Response**](MerchantSubscriptionAdminNoteListGet200Response.md)

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

# **subscription_admin_note_list_post**
> MerchantSubscriptionAdminNoteListGet200Response subscription_admin_note_list_post(unibee_api_merchant_subscription_admin_note_list_req)

Merchant Subscription Note List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_admin_note_list_get200_response import MerchantSubscriptionAdminNoteListGet200Response
from openapi_client.models.unibee_api_merchant_subscription_admin_note_list_req import UnibeeApiMerchantSubscriptionAdminNoteListReq
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
    api_instance = openapi_client.SubscriptionNote(api_client)
    unibee_api_merchant_subscription_admin_note_list_req = openapi_client.UnibeeApiMerchantSubscriptionAdminNoteListReq() # UnibeeApiMerchantSubscriptionAdminNoteListReq | 

    try:
        # Merchant Subscription Note List
        api_response = api_instance.subscription_admin_note_list_post(unibee_api_merchant_subscription_admin_note_list_req)
        print("The response of SubscriptionNote->subscription_admin_note_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionNote->subscription_admin_note_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_admin_note_list_req** | [**UnibeeApiMerchantSubscriptionAdminNoteListReq**](UnibeeApiMerchantSubscriptionAdminNoteListReq.md)|  | 

### Return type

[**MerchantSubscriptionAdminNoteListGet200Response**](MerchantSubscriptionAdminNoteListGet200Response.md)

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

# **subscription_new_admin_note_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_new_admin_note_post(unibee_api_merchant_subscription_new_admin_note_req)

Merchant New Subscription Note

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_new_admin_note_req import UnibeeApiMerchantSubscriptionNewAdminNoteReq
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
    api_instance = openapi_client.SubscriptionNote(api_client)
    unibee_api_merchant_subscription_new_admin_note_req = openapi_client.UnibeeApiMerchantSubscriptionNewAdminNoteReq() # UnibeeApiMerchantSubscriptionNewAdminNoteReq | 

    try:
        # Merchant New Subscription Note
        api_response = api_instance.subscription_new_admin_note_post(unibee_api_merchant_subscription_new_admin_note_req)
        print("The response of SubscriptionNote->subscription_new_admin_note_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionNote->subscription_new_admin_note_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_new_admin_note_req** | [**UnibeeApiMerchantSubscriptionNewAdminNoteReq**](UnibeeApiMerchantSubscriptionNewAdminNoteReq.md)|  | 

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

