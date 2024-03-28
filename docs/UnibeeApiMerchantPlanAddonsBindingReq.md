# UnibeeApiMerchantPlanAddonsBindingReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **int** | Action Type，0-override,1-add，2-delete | 
**addon_ids** | **List[int]** | Plan Ids Of Recurring Addon Type | 
**onetime_addon_ids** | **List[int]** | Plan Ids Of Onetime Addon Type | 
**plan_id** | **int** | PlanID | 

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_addons_binding_req import UnibeeApiMerchantPlanAddonsBindingReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanAddonsBindingReq from a JSON string
unibee_api_merchant_plan_addons_binding_req_instance = UnibeeApiMerchantPlanAddonsBindingReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanAddonsBindingReq.to_json()

# convert the object into a dict
unibee_api_merchant_plan_addons_binding_req_dict = unibee_api_merchant_plan_addons_binding_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanAddonsBindingReq from a dict
unibee_api_merchant_plan_addons_binding_req_form_dict = unibee_api_merchant_plan_addons_binding_req.from_dict(unibee_api_merchant_plan_addons_binding_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


