# UnibeeApiMerchantSubscriptionTimeLineListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_time_lines** | [**List[UnibeeApiBeanSubscriptionTimeLineDetail]**](UnibeeApiBeanSubscriptionTimeLineDetail.md) | SubscriptionTimeLines | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_time_line_list_res import UnibeeApiMerchantSubscriptionTimeLineListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionTimeLineListRes from a JSON string
unibee_api_merchant_subscription_time_line_list_res_instance = UnibeeApiMerchantSubscriptionTimeLineListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionTimeLineListRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_time_line_list_res_dict = unibee_api_merchant_subscription_time_line_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionTimeLineListRes from a dict
unibee_api_merchant_subscription_time_line_list_res_form_dict = unibee_api_merchant_subscription_time_line_list_res.from_dict(unibee_api_merchant_subscription_time_line_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


