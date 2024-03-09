# UnibeeInternalLogicGatewayRoUserMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[UnibeeInternalLogicGatewayRoPlanAddonVo]**](UnibeeInternalLogicGatewayRoPlanAddonVo.md) | Addon | [optional] 
**is_paid** | **bool** | IsPaid | [optional] 
**plan** | [**UnibeeInternalLogicGatewayRoPlanSimplify**](UnibeeInternalLogicGatewayRoPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeInternalLogicGatewayRoSubscriptionSimplify**](UnibeeInternalLogicGatewayRoSubscriptionSimplify.md) |  | [optional] 
**user** | [**UnibeeInternalLogicGatewayRoUserAccountSimplify**](UnibeeInternalLogicGatewayRoUserAccountSimplify.md) |  | [optional] 
**user_merchant_metric_stats** | [**List[UnibeeInternalLogicGatewayRoUserMerchantMetricStat]**](UnibeeInternalLogicGatewayRoUserMerchantMetricStat.md) | UserMerchantMetricStats | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_user_metric import UnibeeInternalLogicGatewayRoUserMetric

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoUserMetric from a JSON string
unibee_internal_logic_gateway_ro_user_metric_instance = UnibeeInternalLogicGatewayRoUserMetric.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoUserMetric.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_user_metric_dict = unibee_internal_logic_gateway_ro_user_metric_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoUserMetric from a dict
unibee_internal_logic_gateway_ro_user_metric_form_dict = unibee_internal_logic_gateway_ro_user_metric.from_dict(unibee_internal_logic_gateway_ro_user_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


