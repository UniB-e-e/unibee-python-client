# MerchantSubscriptionUpdatePreviewPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**invoice** | [**UnibeeInternalLogicGatewayRoInvoiceDetailSimplify**](UnibeeInternalLogicGatewayRoInvoiceDetailSimplify.md) |  | [optional] 
**next_period_invoice** | [**UnibeeInternalLogicGatewayRoInvoiceDetailSimplify**](UnibeeInternalLogicGatewayRoInvoiceDetailSimplify.md) |  | [optional] 
**proration_date** | **int** |  | [optional] 
**total_amount** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_update_preview_post200_response_data import MerchantSubscriptionUpdatePreviewPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionUpdatePreviewPost200ResponseData from a JSON string
merchant_subscription_update_preview_post200_response_data_instance = MerchantSubscriptionUpdatePreviewPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionUpdatePreviewPost200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_update_preview_post200_response_data_dict = merchant_subscription_update_preview_post200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionUpdatePreviewPost200ResponseData from a dict
merchant_subscription_update_preview_post200_response_data_form_dict = merchant_subscription_update_preview_post200_response_data.from_dict(merchant_subscription_update_preview_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


