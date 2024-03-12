# MerchantSubscriptionPendingUpdateListGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_pending_update_details** | [**List[UnibeeApiBeanSubscriptionPendingUpdateDetail]**](UnibeeApiBeanSubscriptionPendingUpdateDetail.md) | SubscriptionPendingUpdateDetails | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_pending_update_list_get200_response_data import MerchantSubscriptionPendingUpdateListGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionPendingUpdateListGet200ResponseData from a JSON string
merchant_subscription_pending_update_list_get200_response_data_instance = MerchantSubscriptionPendingUpdateListGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionPendingUpdateListGet200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_pending_update_list_get200_response_data_dict = merchant_subscription_pending_update_list_get200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionPendingUpdateListGet200ResponseData from a dict
merchant_subscription_pending_update_list_get200_response_data_form_dict = merchant_subscription_pending_update_list_get200_response_data.from_dict(merchant_subscription_pending_update_list_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


