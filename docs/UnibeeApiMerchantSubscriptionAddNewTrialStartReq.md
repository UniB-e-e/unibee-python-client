# UnibeeApiMerchantSubscriptionAddNewTrialStartReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**append_trial_end_hour** | **int** | add appendTrialEndHour For Free | 
**subscription_id** | **str** | SubscriptionId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_add_new_trial_start_req import UnibeeApiMerchantSubscriptionAddNewTrialStartReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionAddNewTrialStartReq from a JSON string
unibee_api_merchant_subscription_add_new_trial_start_req_instance = UnibeeApiMerchantSubscriptionAddNewTrialStartReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionAddNewTrialStartReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_add_new_trial_start_req_dict = unibee_api_merchant_subscription_add_new_trial_start_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionAddNewTrialStartReq from a dict
unibee_api_merchant_subscription_add_new_trial_start_req_form_dict = unibee_api_merchant_subscription_add_new_trial_start_req.from_dict(unibee_api_merchant_subscription_add_new_trial_start_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


