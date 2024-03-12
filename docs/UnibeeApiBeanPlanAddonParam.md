# UnibeeApiBeanPlanAddonParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_plan_id** | **int** | AddonPlanId | [optional] 
**quantity** | **int** | Quantity，Default 1 | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_plan_addon_param import UnibeeApiBeanPlanAddonParam

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPlanAddonParam from a JSON string
unibee_api_bean_plan_addon_param_instance = UnibeeApiBeanPlanAddonParam.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPlanAddonParam.to_json()

# convert the object into a dict
unibee_api_bean_plan_addon_param_dict = unibee_api_bean_plan_addon_param_instance.to_dict()
# create an instance of UnibeeApiBeanPlanAddonParam from a dict
unibee_api_bean_plan_addon_param_form_dict = unibee_api_bean_plan_addon_param.from_dict(unibee_api_bean_plan_addon_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


