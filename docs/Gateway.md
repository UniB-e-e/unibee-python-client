# openapi_client.Gateway

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gateway_edit_country_config_post**](Gateway.md#gateway_edit_country_config_post) | **POST** /merchant/gateway/edit_country_config | Gateway Webhook Edit Country Config
[**gateway_edit_post**](Gateway.md#gateway_edit_post) | **POST** /merchant/gateway/edit | Gateway Webhook Edit
[**gateway_list_get**](Gateway.md#gateway_list_get) | **GET** /merchant/gateway/list | Gateway List
[**gateway_setup_post**](Gateway.md#gateway_setup_post) | **POST** /merchant/gateway/setup | Gateway Setup
[**gateway_setup_webhook_post**](Gateway.md#gateway_setup_webhook_post) | **POST** /merchant/gateway/setup_webhook | Gateway Webhook Setup


# **gateway_edit_country_config_post**
> MerchantAuthSsoLoginOTPPost200Response gateway_edit_country_config_post(unibee_api_merchant_gateway_edit_country_config_req)

Gateway Webhook Edit Country Config

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_gateway_edit_country_config_req import UnibeeApiMerchantGatewayEditCountryConfigReq
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
    api_instance = openapi_client.Gateway(api_client)
    unibee_api_merchant_gateway_edit_country_config_req = openapi_client.UnibeeApiMerchantGatewayEditCountryConfigReq() # UnibeeApiMerchantGatewayEditCountryConfigReq | 

    try:
        # Gateway Webhook Edit Country Config
        api_response = api_instance.gateway_edit_country_config_post(unibee_api_merchant_gateway_edit_country_config_req)
        print("The response of Gateway->gateway_edit_country_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Gateway->gateway_edit_country_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_gateway_edit_country_config_req** | [**UnibeeApiMerchantGatewayEditCountryConfigReq**](UnibeeApiMerchantGatewayEditCountryConfigReq.md)|  | 

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

# **gateway_edit_post**
> MerchantAuthSsoLoginOTPPost200Response gateway_edit_post(unibee_api_merchant_gateway_edit_req)

Gateway Webhook Edit

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_gateway_edit_req import UnibeeApiMerchantGatewayEditReq
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
    api_instance = openapi_client.Gateway(api_client)
    unibee_api_merchant_gateway_edit_req = openapi_client.UnibeeApiMerchantGatewayEditReq() # UnibeeApiMerchantGatewayEditReq | 

    try:
        # Gateway Webhook Edit
        api_response = api_instance.gateway_edit_post(unibee_api_merchant_gateway_edit_req)
        print("The response of Gateway->gateway_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Gateway->gateway_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_gateway_edit_req** | [**UnibeeApiMerchantGatewayEditReq**](UnibeeApiMerchantGatewayEditReq.md)|  | 

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

# **gateway_list_get**
> MerchantGatewayListGet200Response gateway_list_get()

Gateway List

### Example


```python
import openapi_client
from openapi_client.models.merchant_gateway_list_get200_response import MerchantGatewayListGet200Response
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
    api_instance = openapi_client.Gateway(api_client)

    try:
        # Gateway List
        api_response = api_instance.gateway_list_get()
        print("The response of Gateway->gateway_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Gateway->gateway_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantGatewayListGet200Response**](MerchantGatewayListGet200Response.md)

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

# **gateway_setup_post**
> MerchantAuthSsoLoginOTPPost200Response gateway_setup_post(unibee_api_merchant_gateway_setup_req)

Gateway Setup

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_gateway_setup_req import UnibeeApiMerchantGatewaySetupReq
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
    api_instance = openapi_client.Gateway(api_client)
    unibee_api_merchant_gateway_setup_req = openapi_client.UnibeeApiMerchantGatewaySetupReq() # UnibeeApiMerchantGatewaySetupReq | 

    try:
        # Gateway Setup
        api_response = api_instance.gateway_setup_post(unibee_api_merchant_gateway_setup_req)
        print("The response of Gateway->gateway_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Gateway->gateway_setup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_gateway_setup_req** | [**UnibeeApiMerchantGatewaySetupReq**](UnibeeApiMerchantGatewaySetupReq.md)|  | 

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

# **gateway_setup_webhook_post**
> MerchantGatewaySetupWebhookPost200Response gateway_setup_webhook_post(unibee_api_merchant_gateway_setup_webhook_req)

Gateway Webhook Setup

### Example


```python
import openapi_client
from openapi_client.models.merchant_gateway_setup_webhook_post200_response import MerchantGatewaySetupWebhookPost200Response
from openapi_client.models.unibee_api_merchant_gateway_setup_webhook_req import UnibeeApiMerchantGatewaySetupWebhookReq
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
    api_instance = openapi_client.Gateway(api_client)
    unibee_api_merchant_gateway_setup_webhook_req = openapi_client.UnibeeApiMerchantGatewaySetupWebhookReq() # UnibeeApiMerchantGatewaySetupWebhookReq | 

    try:
        # Gateway Webhook Setup
        api_response = api_instance.gateway_setup_webhook_post(unibee_api_merchant_gateway_setup_webhook_req)
        print("The response of Gateway->gateway_setup_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Gateway->gateway_setup_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_gateway_setup_webhook_req** | [**UnibeeApiMerchantGatewaySetupWebhookReq**](UnibeeApiMerchantGatewaySetupWebhookReq.md)|  | 

### Return type

[**MerchantGatewaySetupWebhookPost200Response**](MerchantGatewaySetupWebhookPost200Response.md)

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

