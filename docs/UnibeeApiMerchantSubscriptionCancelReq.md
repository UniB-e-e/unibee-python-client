# UnibeeApiMerchantSubscriptionCancelReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_now** | **bool** | Default false | [optional] 
**prorate** | **bool** | Prorate Generate Invoice，Default false | [optional] 
**subscription_id** | **str** | SubscriptionId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_cancel_req import UnibeeApiMerchantSubscriptionCancelReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionCancelReq from a JSON string
unibee_api_merchant_subscription_cancel_req_instance = UnibeeApiMerchantSubscriptionCancelReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionCancelReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_cancel_req_dict = unibee_api_merchant_subscription_cancel_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionCancelReq from a dict
unibee_api_merchant_subscription_cancel_req_form_dict = unibee_api_merchant_subscription_cancel_req.from_dict(unibee_api_merchant_subscription_cancel_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


