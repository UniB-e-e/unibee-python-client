# openapi_client.SubscriptionPendingUpdate

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_pending_update_list_get**](SubscriptionPendingUpdate.md#subscription_pending_update_list_get) | **GET** /merchant/subscription/pending_update_list | Merchant SubscriptionPendingUpdate List
[**subscription_pending_update_list_post**](SubscriptionPendingUpdate.md#subscription_pending_update_list_post) | **POST** /merchant/subscription/pending_update_list | Merchant SubscriptionPendingUpdate List


# **subscription_pending_update_list_get**
> MerchantSubscriptionPendingUpdateListGet200Response subscription_pending_update_list_get(subscription_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Merchant SubscriptionPendingUpdate List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_pending_update_list_get200_response import MerchantSubscriptionPendingUpdateListGet200Response
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
    api_instance = openapi_client.SubscriptionPendingUpdate(api_client)
    subscription_id = 'subscription_id_example' # str | SubscriptionId
    sort_field = 'sort_field_example' # str | Sort Field，gmt_create|gmt_modify，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page, Start WIth 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Merchant SubscriptionPendingUpdate List
        api_response = api_instance.subscription_pending_update_list_get(subscription_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of SubscriptionPendingUpdate->subscription_pending_update_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPendingUpdate->subscription_pending_update_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| SubscriptionId | 
 **sort_field** | **str**| Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page, Start WIth 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantSubscriptionPendingUpdateListGet200Response**](MerchantSubscriptionPendingUpdateListGet200Response.md)

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

# **subscription_pending_update_list_post**
> MerchantSubscriptionPendingUpdateListGet200Response subscription_pending_update_list_post(unibee_api_merchant_subscription_pending_update_list_req)

Merchant SubscriptionPendingUpdate List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_pending_update_list_get200_response import MerchantSubscriptionPendingUpdateListGet200Response
from openapi_client.models.unibee_api_merchant_subscription_pending_update_list_req import UnibeeApiMerchantSubscriptionPendingUpdateListReq
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
    api_instance = openapi_client.SubscriptionPendingUpdate(api_client)
    unibee_api_merchant_subscription_pending_update_list_req = openapi_client.UnibeeApiMerchantSubscriptionPendingUpdateListReq() # UnibeeApiMerchantSubscriptionPendingUpdateListReq | 

    try:
        # Merchant SubscriptionPendingUpdate List
        api_response = api_instance.subscription_pending_update_list_post(unibee_api_merchant_subscription_pending_update_list_req)
        print("The response of SubscriptionPendingUpdate->subscription_pending_update_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPendingUpdate->subscription_pending_update_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_pending_update_list_req** | [**UnibeeApiMerchantSubscriptionPendingUpdateListReq**](UnibeeApiMerchantSubscriptionPendingUpdateListReq.md)|  | 

### Return type

[**MerchantSubscriptionPendingUpdateListGet200Response**](MerchantSubscriptionPendingUpdateListGet200Response.md)

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

