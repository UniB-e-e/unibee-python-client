# UnibeeApiMerchantSubscriptionUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo]**](UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo.md) | addonParams | [optional] 
**confirm_currency** | **str** | Currency To Be Confirmed，Get From Preview | 
**confirm_total_amount** | **int** | TotalAmount To Be Confirmed，Get From Preview | 
**new_plan_id** | **int** | New PlanId | 
**proration_date** | **int** | prorationDate date to start Proration，Get From Preview | 
**quantity** | **int** | Quantity，Default 1 | [optional] 
**subscription_id** | **str** | SubscriptionId | 
**with_immediate_effect** | **int** | Effect Immediate，1-Immediate，2-Next Period | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_update_req import UnibeeApiMerchantSubscriptionUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionUpdateReq from a JSON string
unibee_api_merchant_subscription_update_req_instance = UnibeeApiMerchantSubscriptionUpdateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionUpdateReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_update_req_dict = unibee_api_merchant_subscription_update_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionUpdateReq from a dict
unibee_api_merchant_subscription_update_req_form_dict = unibee_api_merchant_subscription_update_req.from_dict(unibee_api_merchant_subscription_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


