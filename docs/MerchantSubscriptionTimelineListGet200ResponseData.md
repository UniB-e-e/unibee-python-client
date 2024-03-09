# MerchantSubscriptionTimelineListGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_time_lines** | [**List[UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo]**](UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo.md) | SubscriptionTimeLines | [optional] 

## Example

```python
from openapi_client.models.merchant_subscription_timeline_list_get200_response_data import MerchantSubscriptionTimelineListGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionTimelineListGet200ResponseData from a JSON string
merchant_subscription_timeline_list_get200_response_data_instance = MerchantSubscriptionTimelineListGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionTimelineListGet200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_timeline_list_get200_response_data_dict = merchant_subscription_timeline_list_get200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionTimelineListGet200ResponseData from a dict
merchant_subscription_timeline_list_get200_response_data_form_dict = merchant_subscription_timeline_list_get200_response_data.from_dict(merchant_subscription_timeline_list_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


