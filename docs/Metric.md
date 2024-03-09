# openapi_client.Metric

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_delete_post**](Metric.md#metric_delete_post) | **POST** /merchant/metric/delete | Delete Merchant Metric
[**metric_detail_post**](Metric.md#metric_detail_post) | **POST** /merchant/metric/detail | Merchant Metric Detail
[**metric_edit_post**](Metric.md#metric_edit_post) | **POST** /merchant/metric/edit | Edit Merchant Metric
[**metric_event_delete_post**](Metric.md#metric_event_delete_post) | **POST** /merchant/metric/event/delete | Del Merchant Metric Event
[**metric_event_new_post**](Metric.md#metric_event_new_post) | **POST** /merchant/metric/event/new | Merchant Metric Event
[**metric_list_get**](Metric.md#metric_list_get) | **GET** /merchant/metric/list | Merchant Metric list
[**metric_new_post**](Metric.md#metric_new_post) | **POST** /merchant/metric/new | New Merchant Metric
[**metric_plan_limit_delete_post**](Metric.md#metric_plan_limit_delete_post) | **POST** /merchant/metric/plan/limit/delete | Delete Merchant Metric Plan TotalLimit
[**metric_plan_limit_edit_post**](Metric.md#metric_plan_limit_edit_post) | **POST** /merchant/metric/plan/limit/edit | Edit Merchant Metric Plan TotalLimit
[**metric_plan_limit_new_post**](Metric.md#metric_plan_limit_new_post) | **POST** /merchant/metric/plan/limit/new | New Merchant Metric Plan TotalLimit


# **metric_delete_post**
> MerchantMetricDeletePost200Response metric_delete_post(unibee_api_merchant_metric_delete_req)

Delete Merchant Metric

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_delete_post200_response import MerchantMetricDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_delete_req import UnibeeApiMerchantMetricDeleteReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_delete_req = openapi_client.UnibeeApiMerchantMetricDeleteReq() # UnibeeApiMerchantMetricDeleteReq | 

    try:
        # Delete Merchant Metric
        api_response = api_instance.metric_delete_post(unibee_api_merchant_metric_delete_req)
        print("The response of Metric->metric_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_delete_req** | [**UnibeeApiMerchantMetricDeleteReq**](UnibeeApiMerchantMetricDeleteReq.md)|  | 

### Return type

[**MerchantMetricDeletePost200Response**](MerchantMetricDeletePost200Response.md)

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

# **metric_detail_post**
> MerchantMetricDeletePost200Response metric_detail_post(unibee_api_merchant_metric_detail_req)

Merchant Metric Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_delete_post200_response import MerchantMetricDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_detail_req import UnibeeApiMerchantMetricDetailReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_detail_req = openapi_client.UnibeeApiMerchantMetricDetailReq() # UnibeeApiMerchantMetricDetailReq | 

    try:
        # Merchant Metric Detail
        api_response = api_instance.metric_detail_post(unibee_api_merchant_metric_detail_req)
        print("The response of Metric->metric_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_detail_req** | [**UnibeeApiMerchantMetricDetailReq**](UnibeeApiMerchantMetricDetailReq.md)|  | 

### Return type

[**MerchantMetricDeletePost200Response**](MerchantMetricDeletePost200Response.md)

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

# **metric_edit_post**
> MerchantMetricDeletePost200Response metric_edit_post(unibee_api_merchant_metric_edit_req)

Edit Merchant Metric

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_delete_post200_response import MerchantMetricDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_edit_req import UnibeeApiMerchantMetricEditReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_edit_req = openapi_client.UnibeeApiMerchantMetricEditReq() # UnibeeApiMerchantMetricEditReq | 

    try:
        # Edit Merchant Metric
        api_response = api_instance.metric_edit_post(unibee_api_merchant_metric_edit_req)
        print("The response of Metric->metric_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_edit_req** | [**UnibeeApiMerchantMetricEditReq**](UnibeeApiMerchantMetricEditReq.md)|  | 

### Return type

[**MerchantMetricDeletePost200Response**](MerchantMetricDeletePost200Response.md)

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

# **metric_event_delete_post**
> MerchantAuthSsoLoginOTPPost200Response metric_event_delete_post(unibee_api_merchant_metric_delete_event_req)

Del Merchant Metric Event

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_metric_delete_event_req import UnibeeApiMerchantMetricDeleteEventReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_delete_event_req = openapi_client.UnibeeApiMerchantMetricDeleteEventReq() # UnibeeApiMerchantMetricDeleteEventReq | 

    try:
        # Del Merchant Metric Event
        api_response = api_instance.metric_event_delete_post(unibee_api_merchant_metric_delete_event_req)
        print("The response of Metric->metric_event_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_event_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_delete_event_req** | [**UnibeeApiMerchantMetricDeleteEventReq**](UnibeeApiMerchantMetricDeleteEventReq.md)|  | 

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

# **metric_event_new_post**
> MerchantMetricEventNewPost200Response metric_event_new_post(unibee_api_merchant_metric_new_event_req)

Merchant Metric Event

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_event_new_post200_response import MerchantMetricEventNewPost200Response
from openapi_client.models.unibee_api_merchant_metric_new_event_req import UnibeeApiMerchantMetricNewEventReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_new_event_req = openapi_client.UnibeeApiMerchantMetricNewEventReq() # UnibeeApiMerchantMetricNewEventReq | 

    try:
        # Merchant Metric Event
        api_response = api_instance.metric_event_new_post(unibee_api_merchant_metric_new_event_req)
        print("The response of Metric->metric_event_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_event_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_new_event_req** | [**UnibeeApiMerchantMetricNewEventReq**](UnibeeApiMerchantMetricNewEventReq.md)|  | 

### Return type

[**MerchantMetricEventNewPost200Response**](MerchantMetricEventNewPost200Response.md)

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

# **metric_list_get**
> MerchantMetricListGet200Response metric_list_get()

Merchant Metric list

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_list_get200_response import MerchantMetricListGet200Response
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
    api_instance = openapi_client.Metric(api_client)

    try:
        # Merchant Metric list
        api_response = api_instance.metric_list_get()
        print("The response of Metric->metric_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantMetricListGet200Response**](MerchantMetricListGet200Response.md)

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

# **metric_new_post**
> MerchantMetricDeletePost200Response metric_new_post(unibee_api_merchant_metric_new_req)

New Merchant Metric

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_delete_post200_response import MerchantMetricDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_new_req import UnibeeApiMerchantMetricNewReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_new_req = openapi_client.UnibeeApiMerchantMetricNewReq() # UnibeeApiMerchantMetricNewReq | 

    try:
        # New Merchant Metric
        api_response = api_instance.metric_new_post(unibee_api_merchant_metric_new_req)
        print("The response of Metric->metric_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_new_req** | [**UnibeeApiMerchantMetricNewReq**](UnibeeApiMerchantMetricNewReq.md)|  | 

### Return type

[**MerchantMetricDeletePost200Response**](MerchantMetricDeletePost200Response.md)

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

# **metric_plan_limit_delete_post**
> MerchantMetricPlanLimitDeletePost200Response metric_plan_limit_delete_post(unibee_api_merchant_metric_delete_plan_limit_req)

Delete Merchant Metric Plan TotalLimit

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_plan_limit_delete_post200_response import MerchantMetricPlanLimitDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_delete_plan_limit_req import UnibeeApiMerchantMetricDeletePlanLimitReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_delete_plan_limit_req = openapi_client.UnibeeApiMerchantMetricDeletePlanLimitReq() # UnibeeApiMerchantMetricDeletePlanLimitReq | 

    try:
        # Delete Merchant Metric Plan TotalLimit
        api_response = api_instance.metric_plan_limit_delete_post(unibee_api_merchant_metric_delete_plan_limit_req)
        print("The response of Metric->metric_plan_limit_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_plan_limit_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_delete_plan_limit_req** | [**UnibeeApiMerchantMetricDeletePlanLimitReq**](UnibeeApiMerchantMetricDeletePlanLimitReq.md)|  | 

### Return type

[**MerchantMetricPlanLimitDeletePost200Response**](MerchantMetricPlanLimitDeletePost200Response.md)

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

# **metric_plan_limit_edit_post**
> MerchantMetricPlanLimitDeletePost200Response metric_plan_limit_edit_post(unibee_api_merchant_metric_edit_plan_limit_req)

Edit Merchant Metric Plan TotalLimit

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_plan_limit_delete_post200_response import MerchantMetricPlanLimitDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_edit_plan_limit_req import UnibeeApiMerchantMetricEditPlanLimitReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_edit_plan_limit_req = openapi_client.UnibeeApiMerchantMetricEditPlanLimitReq() # UnibeeApiMerchantMetricEditPlanLimitReq | 

    try:
        # Edit Merchant Metric Plan TotalLimit
        api_response = api_instance.metric_plan_limit_edit_post(unibee_api_merchant_metric_edit_plan_limit_req)
        print("The response of Metric->metric_plan_limit_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_plan_limit_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_edit_plan_limit_req** | [**UnibeeApiMerchantMetricEditPlanLimitReq**](UnibeeApiMerchantMetricEditPlanLimitReq.md)|  | 

### Return type

[**MerchantMetricPlanLimitDeletePost200Response**](MerchantMetricPlanLimitDeletePost200Response.md)

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

# **metric_plan_limit_new_post**
> MerchantMetricPlanLimitDeletePost200Response metric_plan_limit_new_post(unibee_api_merchant_metric_new_plan_limit_req)

New Merchant Metric Plan TotalLimit

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_plan_limit_delete_post200_response import MerchantMetricPlanLimitDeletePost200Response
from openapi_client.models.unibee_api_merchant_metric_new_plan_limit_req import UnibeeApiMerchantMetricNewPlanLimitReq
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
    api_instance = openapi_client.Metric(api_client)
    unibee_api_merchant_metric_new_plan_limit_req = openapi_client.UnibeeApiMerchantMetricNewPlanLimitReq() # UnibeeApiMerchantMetricNewPlanLimitReq | 

    try:
        # New Merchant Metric Plan TotalLimit
        api_response = api_instance.metric_plan_limit_new_post(unibee_api_merchant_metric_new_plan_limit_req)
        print("The response of Metric->metric_plan_limit_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Metric->metric_plan_limit_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_metric_new_plan_limit_req** | [**UnibeeApiMerchantMetricNewPlanLimitReq**](UnibeeApiMerchantMetricNewPlanLimitReq.md)|  | 

### Return type

[**MerchantMetricPlanLimitDeletePost200Response**](MerchantMetricPlanLimitDeletePost200Response.md)

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

