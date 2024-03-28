# openapi_client.Invoice

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoice_cancel_post**](Invoice.md#invoice_cancel_post) | **POST** /merchant/invoice/cancel | Admin Cancel Invoice Of Processing Status
[**invoice_delete_post**](Invoice.md#invoice_delete_post) | **POST** /merchant/invoice/delete | Admin Delete Invoice Of Pending Status
[**invoice_detail_get**](Invoice.md#invoice_detail_get) | **GET** /merchant/invoice/detail | Invoice Detail
[**invoice_detail_post**](Invoice.md#invoice_detail_post) | **POST** /merchant/invoice/detail | Invoice Detail
[**invoice_edit_post**](Invoice.md#invoice_edit_post) | **POST** /merchant/invoice/edit | Admin Edit Invoice
[**invoice_finish_post**](Invoice.md#invoice_finish_post) | **POST** /merchant/invoice/finish | Admin Finish Invoice，Generate Pay Link
[**invoice_list_get**](Invoice.md#invoice_list_get) | **GET** /merchant/invoice/list | Invoice List
[**invoice_list_post**](Invoice.md#invoice_list_post) | **POST** /merchant/invoice/list | Invoice List
[**invoice_mark_refund_post**](Invoice.md#invoice_mark_refund_post) | **POST** /merchant/invoice/mark_refund | Admin Mark Refund For Invoice
[**invoice_new_post**](Invoice.md#invoice_new_post) | **POST** /merchant/invoice/new | Admin Create New Invoice
[**invoice_pdf_generate_post**](Invoice.md#invoice_pdf_generate_post) | **POST** /merchant/invoice/pdf_generate | Admin Generate Merchant Invoice pdf
[**invoice_reconvert_crypto_and_send_email_post**](Invoice.md#invoice_reconvert_crypto_and_send_email_post) | **POST** /merchant/invoice/reconvert_crypto_and_send_email | Admin Reconvert Crypto Data and Send Invoice Email to User
[**invoice_refund_post**](Invoice.md#invoice_refund_post) | **POST** /merchant/invoice/refund | Admin Create Refund For Invoice
[**invoice_send_email_post**](Invoice.md#invoice_send_email_post) | **POST** /merchant/invoice/send_email | Admin Send Merchant Invoice Email to User


# **invoice_cancel_post**
> MerchantAuthSsoLoginOTPPost200Response invoice_cancel_post(unibee_api_merchant_invoice_cancel_req)

Admin Cancel Invoice Of Processing Status

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_invoice_cancel_req import UnibeeApiMerchantInvoiceCancelReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_cancel_req = openapi_client.UnibeeApiMerchantInvoiceCancelReq() # UnibeeApiMerchantInvoiceCancelReq | 

    try:
        # Admin Cancel Invoice Of Processing Status
        api_response = api_instance.invoice_cancel_post(unibee_api_merchant_invoice_cancel_req)
        print("The response of Invoice->invoice_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_cancel_req** | [**UnibeeApiMerchantInvoiceCancelReq**](UnibeeApiMerchantInvoiceCancelReq.md)|  | 

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

# **invoice_delete_post**
> MerchantAuthSsoLoginOTPPost200Response invoice_delete_post(unibee_api_merchant_invoice_delete_req)

Admin Delete Invoice Of Pending Status

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_invoice_delete_req import UnibeeApiMerchantInvoiceDeleteReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_delete_req = openapi_client.UnibeeApiMerchantInvoiceDeleteReq() # UnibeeApiMerchantInvoiceDeleteReq | 

    try:
        # Admin Delete Invoice Of Pending Status
        api_response = api_instance.invoice_delete_post(unibee_api_merchant_invoice_delete_req)
        print("The response of Invoice->invoice_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_delete_req** | [**UnibeeApiMerchantInvoiceDeleteReq**](UnibeeApiMerchantInvoiceDeleteReq.md)|  | 

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

# **invoice_detail_get**
> MerchantInvoiceDetailGet200Response invoice_detail_get(invoice_id)

Invoice Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_detail_get200_response import MerchantInvoiceDetailGet200Response
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
    api_instance = openapi_client.Invoice(api_client)
    invoice_id = 'invoice_id_example' # str | Invoice ID

    try:
        # Invoice Detail
        api_response = api_instance.invoice_detail_get(invoice_id)
        print("The response of Invoice->invoice_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| Invoice ID | 

### Return type

[**MerchantInvoiceDetailGet200Response**](MerchantInvoiceDetailGet200Response.md)

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

# **invoice_detail_post**
> MerchantInvoiceDetailGet200Response invoice_detail_post(unibee_api_merchant_invoice_detail_req)

Invoice Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_detail_get200_response import MerchantInvoiceDetailGet200Response
from openapi_client.models.unibee_api_merchant_invoice_detail_req import UnibeeApiMerchantInvoiceDetailReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_detail_req = openapi_client.UnibeeApiMerchantInvoiceDetailReq() # UnibeeApiMerchantInvoiceDetailReq | 

    try:
        # Invoice Detail
        api_response = api_instance.invoice_detail_post(unibee_api_merchant_invoice_detail_req)
        print("The response of Invoice->invoice_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_detail_req** | [**UnibeeApiMerchantInvoiceDetailReq**](UnibeeApiMerchantInvoiceDetailReq.md)|  | 

### Return type

[**MerchantInvoiceDetailGet200Response**](MerchantInvoiceDetailGet200Response.md)

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

# **invoice_edit_post**
> MerchantInvoiceDetailGet200Response invoice_edit_post(unibee_api_merchant_invoice_edit_req)

Admin Edit Invoice

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_detail_get200_response import MerchantInvoiceDetailGet200Response
from openapi_client.models.unibee_api_merchant_invoice_edit_req import UnibeeApiMerchantInvoiceEditReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_edit_req = openapi_client.UnibeeApiMerchantInvoiceEditReq() # UnibeeApiMerchantInvoiceEditReq | 

    try:
        # Admin Edit Invoice
        api_response = api_instance.invoice_edit_post(unibee_api_merchant_invoice_edit_req)
        print("The response of Invoice->invoice_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_edit_req** | [**UnibeeApiMerchantInvoiceEditReq**](UnibeeApiMerchantInvoiceEditReq.md)|  | 

### Return type

[**MerchantInvoiceDetailGet200Response**](MerchantInvoiceDetailGet200Response.md)

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

# **invoice_finish_post**
> MerchantInvoiceFinishPost200Response invoice_finish_post(unibee_api_merchant_invoice_finish_req)

Admin Finish Invoice，Generate Pay Link

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_finish_post200_response import MerchantInvoiceFinishPost200Response
from openapi_client.models.unibee_api_merchant_invoice_finish_req import UnibeeApiMerchantInvoiceFinishReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_finish_req = openapi_client.UnibeeApiMerchantInvoiceFinishReq() # UnibeeApiMerchantInvoiceFinishReq | 

    try:
        # Admin Finish Invoice，Generate Pay Link
        api_response = api_instance.invoice_finish_post(unibee_api_merchant_invoice_finish_req)
        print("The response of Invoice->invoice_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_finish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_finish_req** | [**UnibeeApiMerchantInvoiceFinishReq**](UnibeeApiMerchantInvoiceFinishReq.md)|  | 

### Return type

[**MerchantInvoiceFinishPost200Response**](MerchantInvoiceFinishPost200Response.md)

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

# **invoice_list_get**
> MerchantInvoiceListGet200Response invoice_list_get(first_name=first_name, last_name=last_name, currency=currency, status=status, amount_start=amount_start, amount_end=amount_end, user_id=user_id, send_email=send_email, sort_field=sort_field, sort_type=sort_type, delete_include=delete_include, page=page, count=count)

Invoice List

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_list_get200_response import MerchantInvoiceListGet200Response
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
    api_instance = openapi_client.Invoice(api_client)
    first_name = 'first_name_example' # str | FirstName (optional)
    last_name = 'last_name_example' # str | LastName (optional)
    currency = 'currency_example' # str | Currency (optional)
    status = [56] # List[int] | Status, 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled (optional)
    amount_start = 56 # int | AmountStart (optional)
    amount_end = 56 # int | AmountEnd (optional)
    user_id = 56 # int | UserId Filter, Default Filter All (optional)
    send_email = 'send_email_example' # str | SendEmail Filter , Default Filter All (optional)
    sort_field = 'sort_field_example' # str | Filter，em. invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort，asc|desc，Default desc (optional)
    delete_include = True # bool | Deleted Involved，Need Admin (optional)
    page = 56 # int | Page, Start 0 (optional)
    count = 56 # int | Count By Page (optional)

    try:
        # Invoice List
        api_response = api_instance.invoice_list_get(first_name=first_name, last_name=last_name, currency=currency, status=status, amount_start=amount_start, amount_end=amount_end, user_id=user_id, send_email=send_email, sort_field=sort_field, sort_type=sort_type, delete_include=delete_include, page=page, count=count)
        print("The response of Invoice->invoice_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| FirstName | [optional] 
 **last_name** | **str**| LastName | [optional] 
 **currency** | **str**| Currency | [optional] 
 **status** | [**List[int]**](int.md)| Status, 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled | [optional] 
 **amount_start** | **int**| AmountStart | [optional] 
 **amount_end** | **int**| AmountEnd | [optional] 
 **user_id** | **int**| UserId Filter, Default Filter All | [optional] 
 **send_email** | **str**| SendEmail Filter , Default Filter All | [optional] 
 **sort_field** | **str**| Filter，em. invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort，asc|desc，Default desc | [optional] 
 **delete_include** | **bool**| Deleted Involved，Need Admin | [optional] 
 **page** | **int**| Page, Start 0 | [optional] 
 **count** | **int**| Count By Page | [optional] 

### Return type

[**MerchantInvoiceListGet200Response**](MerchantInvoiceListGet200Response.md)

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

# **invoice_list_post**
> MerchantInvoiceListGet200Response invoice_list_post(unibee_api_merchant_invoice_list_req)

Invoice List

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_list_get200_response import MerchantInvoiceListGet200Response
from openapi_client.models.unibee_api_merchant_invoice_list_req import UnibeeApiMerchantInvoiceListReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_list_req = openapi_client.UnibeeApiMerchantInvoiceListReq() # UnibeeApiMerchantInvoiceListReq | 

    try:
        # Invoice List
        api_response = api_instance.invoice_list_post(unibee_api_merchant_invoice_list_req)
        print("The response of Invoice->invoice_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_list_req** | [**UnibeeApiMerchantInvoiceListReq**](UnibeeApiMerchantInvoiceListReq.md)|  | 

### Return type

[**MerchantInvoiceListGet200Response**](MerchantInvoiceListGet200Response.md)

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

# **invoice_mark_refund_post**
> MerchantInvoiceMarkRefundPost200Response invoice_mark_refund_post(unibee_api_merchant_invoice_mark_refund_req)

Admin Mark Refund For Invoice

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_mark_refund_post200_response import MerchantInvoiceMarkRefundPost200Response
from openapi_client.models.unibee_api_merchant_invoice_mark_refund_req import UnibeeApiMerchantInvoiceMarkRefundReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_mark_refund_req = openapi_client.UnibeeApiMerchantInvoiceMarkRefundReq() # UnibeeApiMerchantInvoiceMarkRefundReq | 

    try:
        # Admin Mark Refund For Invoice
        api_response = api_instance.invoice_mark_refund_post(unibee_api_merchant_invoice_mark_refund_req)
        print("The response of Invoice->invoice_mark_refund_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_mark_refund_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_mark_refund_req** | [**UnibeeApiMerchantInvoiceMarkRefundReq**](UnibeeApiMerchantInvoiceMarkRefundReq.md)|  | 

### Return type

[**MerchantInvoiceMarkRefundPost200Response**](MerchantInvoiceMarkRefundPost200Response.md)

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

# **invoice_new_post**
> MerchantInvoiceDetailGet200Response invoice_new_post(unibee_api_merchant_invoice_new_req)

Admin Create New Invoice

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_detail_get200_response import MerchantInvoiceDetailGet200Response
from openapi_client.models.unibee_api_merchant_invoice_new_req import UnibeeApiMerchantInvoiceNewReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_new_req = openapi_client.UnibeeApiMerchantInvoiceNewReq() # UnibeeApiMerchantInvoiceNewReq | 

    try:
        # Admin Create New Invoice
        api_response = api_instance.invoice_new_post(unibee_api_merchant_invoice_new_req)
        print("The response of Invoice->invoice_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_new_req** | [**UnibeeApiMerchantInvoiceNewReq**](UnibeeApiMerchantInvoiceNewReq.md)|  | 

### Return type

[**MerchantInvoiceDetailGet200Response**](MerchantInvoiceDetailGet200Response.md)

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

# **invoice_pdf_generate_post**
> MerchantAuthSsoLoginOTPPost200Response invoice_pdf_generate_post(unibee_api_merchant_invoice_pdf_generate_req)

Admin Generate Merchant Invoice pdf

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_invoice_pdf_generate_req import UnibeeApiMerchantInvoicePdfGenerateReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_pdf_generate_req = openapi_client.UnibeeApiMerchantInvoicePdfGenerateReq() # UnibeeApiMerchantInvoicePdfGenerateReq | 

    try:
        # Admin Generate Merchant Invoice pdf
        api_response = api_instance.invoice_pdf_generate_post(unibee_api_merchant_invoice_pdf_generate_req)
        print("The response of Invoice->invoice_pdf_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_pdf_generate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_pdf_generate_req** | [**UnibeeApiMerchantInvoicePdfGenerateReq**](UnibeeApiMerchantInvoicePdfGenerateReq.md)|  | 

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

# **invoice_reconvert_crypto_and_send_email_post**
> MerchantAuthSsoLoginOTPPost200Response invoice_reconvert_crypto_and_send_email_post(unibee_api_merchant_invoice_reconvert_crypto_and_send_req)

Admin Reconvert Crypto Data and Send Invoice Email to User

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_invoice_reconvert_crypto_and_send_req import UnibeeApiMerchantInvoiceReconvertCryptoAndSendReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_reconvert_crypto_and_send_req = openapi_client.UnibeeApiMerchantInvoiceReconvertCryptoAndSendReq() # UnibeeApiMerchantInvoiceReconvertCryptoAndSendReq | 

    try:
        # Admin Reconvert Crypto Data and Send Invoice Email to User
        api_response = api_instance.invoice_reconvert_crypto_and_send_email_post(unibee_api_merchant_invoice_reconvert_crypto_and_send_req)
        print("The response of Invoice->invoice_reconvert_crypto_and_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_reconvert_crypto_and_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_reconvert_crypto_and_send_req** | [**UnibeeApiMerchantInvoiceReconvertCryptoAndSendReq**](UnibeeApiMerchantInvoiceReconvertCryptoAndSendReq.md)|  | 

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

# **invoice_refund_post**
> MerchantInvoiceMarkRefundPost200Response invoice_refund_post(unibee_api_merchant_invoice_refund_req)

Admin Create Refund For Invoice

### Example


```python
import openapi_client
from openapi_client.models.merchant_invoice_mark_refund_post200_response import MerchantInvoiceMarkRefundPost200Response
from openapi_client.models.unibee_api_merchant_invoice_refund_req import UnibeeApiMerchantInvoiceRefundReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_refund_req = openapi_client.UnibeeApiMerchantInvoiceRefundReq() # UnibeeApiMerchantInvoiceRefundReq | 

    try:
        # Admin Create Refund For Invoice
        api_response = api_instance.invoice_refund_post(unibee_api_merchant_invoice_refund_req)
        print("The response of Invoice->invoice_refund_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_refund_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_refund_req** | [**UnibeeApiMerchantInvoiceRefundReq**](UnibeeApiMerchantInvoiceRefundReq.md)|  | 

### Return type

[**MerchantInvoiceMarkRefundPost200Response**](MerchantInvoiceMarkRefundPost200Response.md)

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

# **invoice_send_email_post**
> MerchantAuthSsoLoginOTPPost200Response invoice_send_email_post(unibee_api_merchant_invoice_send_email_req)

Admin Send Merchant Invoice Email to User

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_invoice_send_email_req import UnibeeApiMerchantInvoiceSendEmailReq
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
    api_instance = openapi_client.Invoice(api_client)
    unibee_api_merchant_invoice_send_email_req = openapi_client.UnibeeApiMerchantInvoiceSendEmailReq() # UnibeeApiMerchantInvoiceSendEmailReq | 

    try:
        # Admin Send Merchant Invoice Email to User
        api_response = api_instance.invoice_send_email_post(unibee_api_merchant_invoice_send_email_req)
        print("The response of Invoice->invoice_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Invoice->invoice_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_invoice_send_email_req** | [**UnibeeApiMerchantInvoiceSendEmailReq**](UnibeeApiMerchantInvoiceSendEmailReq.md)|  | 

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

