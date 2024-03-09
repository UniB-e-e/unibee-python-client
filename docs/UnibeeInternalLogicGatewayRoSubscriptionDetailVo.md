# UnibeeInternalLogicGatewayRoSubscriptionDetailVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo]**](UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo.md) | AddonParams | [optional] 
**addons** | [**List[UnibeeInternalLogicGatewayRoPlanAddonVo]**](UnibeeInternalLogicGatewayRoPlanAddonVo.md) | Addon | [optional] 
**gateway** | [**UnibeeInternalLogicGatewayRoGatewaySimplify**](UnibeeInternalLogicGatewayRoGatewaySimplify.md) |  | [optional] 
**plan** | [**UnibeeInternalLogicGatewayRoPlanSimplify**](UnibeeInternalLogicGatewayRoPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeInternalLogicGatewayRoSubscriptionSimplify**](UnibeeInternalLogicGatewayRoSubscriptionSimplify.md) |  | [optional] 
**unfinished_subscription_pending_update** | [**UnibeeInternalLogicGatewayRoSubscriptionPendingUpdateDetailVo**](UnibeeInternalLogicGatewayRoSubscriptionPendingUpdateDetailVo.md) |  | [optional] 
**user** | [**UnibeeInternalLogicGatewayRoUserAccountSimplify**](UnibeeInternalLogicGatewayRoUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_detail_vo import UnibeeInternalLogicGatewayRoSubscriptionDetailVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoSubscriptionDetailVo from a JSON string
unibee_internal_logic_gateway_ro_subscription_detail_vo_instance = UnibeeInternalLogicGatewayRoSubscriptionDetailVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoSubscriptionDetailVo.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_subscription_detail_vo_dict = unibee_internal_logic_gateway_ro_subscription_detail_vo_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoSubscriptionDetailVo from a dict
unibee_internal_logic_gateway_ro_subscription_detail_vo_form_dict = unibee_internal_logic_gateway_ro_subscription_detail_vo.from_dict(unibee_internal_logic_gateway_ro_subscription_detail_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


