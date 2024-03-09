# UnibeeInternalLogicGatewayRoPlanSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | amount, cent, without tax | [optional] 
**binding_addon_ids** | **str** | binded addon planIds，split with , | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**description** | **str** | description | [optional] 
**extra_metric_data** | **str** |  | [optional] 
**home_url** | **str** | home_url | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** | image_url | [optional] 
**interval_count** | **int** | period unit count | [optional] 
**interval_unit** | **str** | period unit,day|month|year|week | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**plan_name** | **str** | PlanName | [optional] 
**product_description** | **str** | product description | [optional] 
**product_name** | **str** | product name | [optional] 
**publish_status** | **int** | 1-UnPublish,2-Publish, Use For Display Plan At UserPortal | [optional] 
**status** | **int** | status，1-editing，2-active，3-inactive，4-expired | [optional] 
**tax_scale** | **int** | tax scale 1000 &#x3D; 10% | [optional] 
**type** | **int** | type，1-main plan，2-addon plan | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_logic_gateway_ro_plan_simplify import UnibeeInternalLogicGatewayRoPlanSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalLogicGatewayRoPlanSimplify from a JSON string
unibee_internal_logic_gateway_ro_plan_simplify_instance = UnibeeInternalLogicGatewayRoPlanSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalLogicGatewayRoPlanSimplify.to_json()

# convert the object into a dict
unibee_internal_logic_gateway_ro_plan_simplify_dict = unibee_internal_logic_gateway_ro_plan_simplify_instance.to_dict()
# create an instance of UnibeeInternalLogicGatewayRoPlanSimplify from a dict
unibee_internal_logic_gateway_ro_plan_simplify_form_dict = unibee_internal_logic_gateway_ro_plan_simplify.from_dict(unibee_internal_logic_gateway_ro_plan_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


