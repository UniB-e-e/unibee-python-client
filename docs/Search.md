# openapi_client.Search

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_key_search_get**](Search.md#search_key_search_get) | **GET** /merchant/search/key_search | Merchant Search
[**search_key_search_post**](Search.md#search_key_search_post) | **POST** /merchant/search/key_search | Merchant Search


# **search_key_search_get**
> MerchantSearchKeySearchGet200Response search_key_search_get(search_key=search_key)

Merchant Search

### Example


```python
import openapi_client
from openapi_client.models.merchant_search_key_search_get200_response import MerchantSearchKeySearchGet200Response
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
    api_instance = openapi_client.Search(api_client)
    search_key = 'search_key_example' # str | SearchKey, Will Search UserId|Email|UserName|CompanyName|SubscriptionId|VatNumber|InvoiceId||PaymentId (optional)

    try:
        # Merchant Search
        api_response = api_instance.search_key_search_get(search_key=search_key)
        print("The response of Search->search_key_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Search->search_key_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**| SearchKey, Will Search UserId|Email|UserName|CompanyName|SubscriptionId|VatNumber|InvoiceId||PaymentId | [optional] 

### Return type

[**MerchantSearchKeySearchGet200Response**](MerchantSearchKeySearchGet200Response.md)

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

# **search_key_search_post**
> MerchantSearchKeySearchGet200Response search_key_search_post(unibee_api_merchant_search_search_req)

Merchant Search

### Example


```python
import openapi_client
from openapi_client.models.merchant_search_key_search_get200_response import MerchantSearchKeySearchGet200Response
from openapi_client.models.unibee_api_merchant_search_search_req import UnibeeApiMerchantSearchSearchReq
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
    api_instance = openapi_client.Search(api_client)
    unibee_api_merchant_search_search_req = openapi_client.UnibeeApiMerchantSearchSearchReq() # UnibeeApiMerchantSearchSearchReq | 

    try:
        # Merchant Search
        api_response = api_instance.search_key_search_post(unibee_api_merchant_search_search_req)
        print("The response of Search->search_key_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Search->search_key_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_search_search_req** | [**UnibeeApiMerchantSearchSearchReq**](UnibeeApiMerchantSearchSearchReq.md)|  | 

### Return type

[**MerchantSearchKeySearchGet200Response**](MerchantSearchKeySearchGet200Response.md)

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

