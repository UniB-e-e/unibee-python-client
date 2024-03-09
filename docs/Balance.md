# openapi_client.Balance

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_merchant_balance_query_get**](Balance.md#balance_merchant_balance_query_get) | **GET** /merchant/balance/merchant_balance_query | Query Merchant Gateway Balance
[**balance_merchant_balance_query_post**](Balance.md#balance_merchant_balance_query_post) | **POST** /merchant/balance/merchant_balance_query | Query Merchant Gateway Balance
[**balance_user_balance_query_get**](Balance.md#balance_user_balance_query_get) | **GET** /merchant/balance/user_balance_query | Query User Balance
[**balance_user_balance_query_post**](Balance.md#balance_user_balance_query_post) | **POST** /merchant/balance/user_balance_query | Query User Balance


# **balance_merchant_balance_query_get**
> MerchantBalanceMerchantBalanceQueryGet200Response balance_merchant_balance_query_get(gateway_id)

Query Merchant Gateway Balance

### Example


```python
import openapi_client
from openapi_client.models.merchant_balance_merchant_balance_query_get200_response import MerchantBalanceMerchantBalanceQueryGet200Response
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
    api_instance = openapi_client.Balance(api_client)
    gateway_id = 56 # int | gatewayId

    try:
        # Query Merchant Gateway Balance
        api_response = api_instance.balance_merchant_balance_query_get(gateway_id)
        print("The response of Balance->balance_merchant_balance_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Balance->balance_merchant_balance_query_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| gatewayId | 

### Return type

[**MerchantBalanceMerchantBalanceQueryGet200Response**](MerchantBalanceMerchantBalanceQueryGet200Response.md)

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

# **balance_merchant_balance_query_post**
> MerchantBalanceMerchantBalanceQueryGet200Response balance_merchant_balance_query_post(unibee_api_merchant_balance_detail_query_req)

Query Merchant Gateway Balance

### Example


```python
import openapi_client
from openapi_client.models.merchant_balance_merchant_balance_query_get200_response import MerchantBalanceMerchantBalanceQueryGet200Response
from openapi_client.models.unibee_api_merchant_balance_detail_query_req import UnibeeApiMerchantBalanceDetailQueryReq
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
    api_instance = openapi_client.Balance(api_client)
    unibee_api_merchant_balance_detail_query_req = openapi_client.UnibeeApiMerchantBalanceDetailQueryReq() # UnibeeApiMerchantBalanceDetailQueryReq | 

    try:
        # Query Merchant Gateway Balance
        api_response = api_instance.balance_merchant_balance_query_post(unibee_api_merchant_balance_detail_query_req)
        print("The response of Balance->balance_merchant_balance_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Balance->balance_merchant_balance_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_balance_detail_query_req** | [**UnibeeApiMerchantBalanceDetailQueryReq**](UnibeeApiMerchantBalanceDetailQueryReq.md)|  | 

### Return type

[**MerchantBalanceMerchantBalanceQueryGet200Response**](MerchantBalanceMerchantBalanceQueryGet200Response.md)

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

# **balance_user_balance_query_get**
> MerchantBalanceUserBalanceQueryGet200Response balance_user_balance_query_get(user_id, gateway_id)

Query User Balance

### Example


```python
import openapi_client
from openapi_client.models.merchant_balance_user_balance_query_get200_response import MerchantBalanceUserBalanceQueryGet200Response
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
    api_instance = openapi_client.Balance(api_client)
    user_id = 56 # int | userId
    gateway_id = 56 # int | gatewayId

    try:
        # Query User Balance
        api_response = api_instance.balance_user_balance_query_get(user_id, gateway_id)
        print("The response of Balance->balance_user_balance_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Balance->balance_user_balance_query_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | 
 **gateway_id** | **int**| gatewayId | 

### Return type

[**MerchantBalanceUserBalanceQueryGet200Response**](MerchantBalanceUserBalanceQueryGet200Response.md)

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

# **balance_user_balance_query_post**
> MerchantBalanceUserBalanceQueryGet200Response balance_user_balance_query_post(unibee_api_merchant_balance_user_detail_query_req)

Query User Balance

### Example


```python
import openapi_client
from openapi_client.models.merchant_balance_user_balance_query_get200_response import MerchantBalanceUserBalanceQueryGet200Response
from openapi_client.models.unibee_api_merchant_balance_user_detail_query_req import UnibeeApiMerchantBalanceUserDetailQueryReq
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
    api_instance = openapi_client.Balance(api_client)
    unibee_api_merchant_balance_user_detail_query_req = openapi_client.UnibeeApiMerchantBalanceUserDetailQueryReq() # UnibeeApiMerchantBalanceUserDetailQueryReq | 

    try:
        # Query User Balance
        api_response = api_instance.balance_user_balance_query_post(unibee_api_merchant_balance_user_detail_query_req)
        print("The response of Balance->balance_user_balance_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Balance->balance_user_balance_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_balance_user_detail_query_req** | [**UnibeeApiMerchantBalanceUserDetailQueryReq**](UnibeeApiMerchantBalanceUserDetailQueryReq.md)|  | 

### Return type

[**MerchantBalanceUserBalanceQueryGet200Response**](MerchantBalanceUserBalanceQueryGet200Response.md)

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

