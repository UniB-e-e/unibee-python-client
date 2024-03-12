# UnibeeApiMerchantSubscriptionUpdatePreviewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**next_period_invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**proration_date** | **int** |  | [optional] 
**total_amount** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_update_preview_res import UnibeeApiMerchantSubscriptionUpdatePreviewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionUpdatePreviewRes from a JSON string
unibee_api_merchant_subscription_update_preview_res_instance = UnibeeApiMerchantSubscriptionUpdatePreviewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionUpdatePreviewRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_update_preview_res_dict = unibee_api_merchant_subscription_update_preview_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionUpdatePreviewRes from a dict
unibee_api_merchant_subscription_update_preview_res_form_dict = unibee_api_merchant_subscription_update_preview_res.from_dict(unibee_api_merchant_subscription_update_preview_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


