# openapi_client.Email

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_gateway_setup_post**](Email.md#email_gateway_setup_post) | **POST** /merchant/email/gateway_setup | Merchant Email Gateway Setup


# **email_gateway_setup_post**
> MerchantAuthSsoLoginOTPPost200Response email_gateway_setup_post(unibee_api_merchant_email_gateway_setup_req)

Merchant Email Gateway Setup

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_email_gateway_setup_req import UnibeeApiMerchantEmailGatewaySetupReq
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
    api_instance = openapi_client.Email(api_client)
    unibee_api_merchant_email_gateway_setup_req = openapi_client.UnibeeApiMerchantEmailGatewaySetupReq() # UnibeeApiMerchantEmailGatewaySetupReq | 

    try:
        # Merchant Email Gateway Setup
        api_response = api_instance.email_gateway_setup_post(unibee_api_merchant_email_gateway_setup_req)
        print("The response of Email->email_gateway_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Email->email_gateway_setup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_email_gateway_setup_req** | [**UnibeeApiMerchantEmailGatewaySetupReq**](UnibeeApiMerchantEmailGatewaySetupReq.md)|  | 

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

