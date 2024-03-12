# UnibeeApiBeanPlanAddonDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**quantity** | **int** | Quantity | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_plan_addon_detail import UnibeeApiBeanPlanAddonDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPlanAddonDetail from a JSON string
unibee_api_bean_plan_addon_detail_instance = UnibeeApiBeanPlanAddonDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPlanAddonDetail.to_json()

# convert the object into a dict
unibee_api_bean_plan_addon_detail_dict = unibee_api_bean_plan_addon_detail_instance.to_dict()
# create an instance of UnibeeApiBeanPlanAddonDetail from a dict
unibee_api_bean_plan_addon_detail_form_dict = unibee_api_bean_plan_addon_detail.from_dict(unibee_api_bean_plan_addon_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


