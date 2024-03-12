# MerchantSubscriptionUpdateSubmitPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**subscription_pending_update** | [**UnibeeApiBeanSubscriptionPendingUpdateDetail**](UnibeeApiBeanSubscriptionPendingUpdateDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_update_submit_post200_response_data import MerchantSubscriptionUpdateSubmitPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionUpdateSubmitPost200ResponseData from a JSON string
merchant_subscription_update_submit_post200_response_data_instance = MerchantSubscriptionUpdateSubmitPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionUpdateSubmitPost200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_update_submit_post200_response_data_dict = merchant_subscription_update_submit_post200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionUpdateSubmitPost200ResponseData from a dict
merchant_subscription_update_submit_post200_response_data_form_dict = merchant_subscription_update_submit_post200_response_data.from_dict(merchant_subscription_update_submit_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


