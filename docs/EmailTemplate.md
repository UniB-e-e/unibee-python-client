# openapi_client.EmailTemplate

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_template_activate_post**](EmailTemplate.md#email_template_activate_post) | **POST** /merchant/email/template_activate | Merchant Email Template Activate
[**email_template_deactivate_post**](EmailTemplate.md#email_template_deactivate_post) | **POST** /merchant/email/template_deactivate | Merchant Email Template Deactivate
[**email_template_list_get**](EmailTemplate.md#email_template_list_get) | **GET** /merchant/email/template_list | Merchant Email Template List
[**email_template_set_default_post**](EmailTemplate.md#email_template_set_default_post) | **POST** /merchant/email/template_set_default | Merchant Email Template Set Default
[**email_template_update_post**](EmailTemplate.md#email_template_update_post) | **POST** /merchant/email/template_update | Merchant Email Template Update


# **email_template_activate_post**
> MerchantAuthSsoLoginOTPPost200Response email_template_activate_post(unibee_api_merchant_email_template_activate_req)

Merchant Email Template Activate

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_email_template_activate_req import UnibeeApiMerchantEmailTemplateActivateReq
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
    api_instance = openapi_client.EmailTemplate(api_client)
    unibee_api_merchant_email_template_activate_req = openapi_client.UnibeeApiMerchantEmailTemplateActivateReq() # UnibeeApiMerchantEmailTemplateActivateReq | 

    try:
        # Merchant Email Template Activate
        api_response = api_instance.email_template_activate_post(unibee_api_merchant_email_template_activate_req)
        print("The response of EmailTemplate->email_template_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplate->email_template_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_email_template_activate_req** | [**UnibeeApiMerchantEmailTemplateActivateReq**](UnibeeApiMerchantEmailTemplateActivateReq.md)|  | 

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

# **email_template_deactivate_post**
> MerchantAuthSsoLoginOTPPost200Response email_template_deactivate_post(unibee_api_merchant_email_template_deactivate_req)

Merchant Email Template Deactivate

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_email_template_deactivate_req import UnibeeApiMerchantEmailTemplateDeactivateReq
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
    api_instance = openapi_client.EmailTemplate(api_client)
    unibee_api_merchant_email_template_deactivate_req = openapi_client.UnibeeApiMerchantEmailTemplateDeactivateReq() # UnibeeApiMerchantEmailTemplateDeactivateReq | 

    try:
        # Merchant Email Template Deactivate
        api_response = api_instance.email_template_deactivate_post(unibee_api_merchant_email_template_deactivate_req)
        print("The response of EmailTemplate->email_template_deactivate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplate->email_template_deactivate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_email_template_deactivate_req** | [**UnibeeApiMerchantEmailTemplateDeactivateReq**](UnibeeApiMerchantEmailTemplateDeactivateReq.md)|  | 

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

# **email_template_list_get**
> MerchantEmailTemplateListGet200Response email_template_list_get()

Merchant Email Template List

### Example


```python
import openapi_client
from openapi_client.models.merchant_email_template_list_get200_response import MerchantEmailTemplateListGet200Response
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
    api_instance = openapi_client.EmailTemplate(api_client)

    try:
        # Merchant Email Template List
        api_response = api_instance.email_template_list_get()
        print("The response of EmailTemplate->email_template_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplate->email_template_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantEmailTemplateListGet200Response**](MerchantEmailTemplateListGet200Response.md)

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

# **email_template_set_default_post**
> MerchantAuthSsoLoginOTPPost200Response email_template_set_default_post(unibee_api_merchant_email_template_set_default_req)

Merchant Email Template Set Default

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_email_template_set_default_req import UnibeeApiMerchantEmailTemplateSetDefaultReq
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
    api_instance = openapi_client.EmailTemplate(api_client)
    unibee_api_merchant_email_template_set_default_req = openapi_client.UnibeeApiMerchantEmailTemplateSetDefaultReq() # UnibeeApiMerchantEmailTemplateSetDefaultReq | 

    try:
        # Merchant Email Template Set Default
        api_response = api_instance.email_template_set_default_post(unibee_api_merchant_email_template_set_default_req)
        print("The response of EmailTemplate->email_template_set_default_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplate->email_template_set_default_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_email_template_set_default_req** | [**UnibeeApiMerchantEmailTemplateSetDefaultReq**](UnibeeApiMerchantEmailTemplateSetDefaultReq.md)|  | 

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

# **email_template_update_post**
> MerchantAuthSsoLoginOTPPost200Response email_template_update_post(unibee_api_merchant_email_template_update_req)

Merchant Email Template Update

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_email_template_update_req import UnibeeApiMerchantEmailTemplateUpdateReq
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
    api_instance = openapi_client.EmailTemplate(api_client)
    unibee_api_merchant_email_template_update_req = openapi_client.UnibeeApiMerchantEmailTemplateUpdateReq() # UnibeeApiMerchantEmailTemplateUpdateReq | 

    try:
        # Merchant Email Template Update
        api_response = api_instance.email_template_update_post(unibee_api_merchant_email_template_update_req)
        print("The response of EmailTemplate->email_template_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplate->email_template_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_email_template_update_req** | [**UnibeeApiMerchantEmailTemplateUpdateReq**](UnibeeApiMerchantEmailTemplateUpdateReq.md)|  | 

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

