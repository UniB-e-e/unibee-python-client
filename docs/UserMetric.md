# openapi_client.UserMetric

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metric_user_metric_get**](UserMetric.md#metric_user_metric_get) | **GET** /merchant/metric/user/metric | Query User Metric


# **metric_user_metric_get**
> MerchantMetricUserMetricGet200Response metric_user_metric_get(user_id=user_id, external_user_id=external_user_id)

Query User Metric

### Example


```python
import openapi_client
from openapi_client.models.merchant_metric_user_metric_get200_response import MerchantMetricUserMetricGet200Response
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
    api_instance = openapi_client.UserMetric(api_client)
    user_id = 56 # int | UserId, One Of UserId|ExternalUserId Needed (optional)
    external_user_id = 'external_user_id_example' # str | ExternalUserId, One Of UserId|ExternalUserId Needed (optional)

    try:
        # Query User Metric
        api_response = api_instance.metric_user_metric_get(user_id=user_id, external_user_id=external_user_id)
        print("The response of UserMetric->metric_user_metric_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMetric->metric_user_metric_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| UserId, One Of UserId|ExternalUserId Needed | [optional] 
 **external_user_id** | **str**| ExternalUserId, One Of UserId|ExternalUserId Needed | [optional] 

### Return type

[**MerchantMetricUserMetricGet200Response**](MerchantMetricUserMetricGet200Response.md)

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

