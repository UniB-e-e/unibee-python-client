# openapi_client.SubscriptionTimeline

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_timeline_list_get**](SubscriptionTimeline.md#subscription_timeline_list_get) | **GET** /merchant/subscription/timeline_list | Merchant Subscription TimeLine List
[**subscription_timeline_list_post**](SubscriptionTimeline.md#subscription_timeline_list_post) | **POST** /merchant/subscription/timeline_list | Merchant Subscription TimeLine List


# **subscription_timeline_list_get**
> MerchantSubscriptionTimelineListGet200Response subscription_timeline_list_get(user_id=user_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Merchant Subscription TimeLine List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_timeline_list_get200_response import MerchantSubscriptionTimelineListGet200Response
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
    api_instance = openapi_client.SubscriptionTimeline(api_client)
    user_id = 56 # int | Filter UserId, Default All  (optional)
    sort_field = 'sort_field_example' # str | Sort Field，gmt_create|gmt_modify，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page, Start WIth 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Merchant Subscription TimeLine List
        api_response = api_instance.subscription_timeline_list_get(user_id=user_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of SubscriptionTimeline->subscription_timeline_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTimeline->subscription_timeline_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Filter UserId, Default All  | [optional] 
 **sort_field** | **str**| Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page, Start WIth 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantSubscriptionTimelineListGet200Response**](MerchantSubscriptionTimelineListGet200Response.md)

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

# **subscription_timeline_list_post**
> MerchantSubscriptionTimelineListGet200Response subscription_timeline_list_post(unibee_api_merchant_subscription_time_line_list_req)

Merchant Subscription TimeLine List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_timeline_list_get200_response import MerchantSubscriptionTimelineListGet200Response
from openapi_client.models.unibee_api_merchant_subscription_time_line_list_req import UnibeeApiMerchantSubscriptionTimeLineListReq
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
    api_instance = openapi_client.SubscriptionTimeline(api_client)
    unibee_api_merchant_subscription_time_line_list_req = openapi_client.UnibeeApiMerchantSubscriptionTimeLineListReq() # UnibeeApiMerchantSubscriptionTimeLineListReq | 

    try:
        # Merchant Subscription TimeLine List
        api_response = api_instance.subscription_timeline_list_post(unibee_api_merchant_subscription_time_line_list_req)
        print("The response of SubscriptionTimeline->subscription_timeline_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTimeline->subscription_timeline_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_time_line_list_req** | [**UnibeeApiMerchantSubscriptionTimeLineListReq**](UnibeeApiMerchantSubscriptionTimeLineListReq.md)|  | 

### Return type

[**MerchantSubscriptionTimelineListGet200Response**](MerchantSubscriptionTimelineListGet200Response.md)

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

