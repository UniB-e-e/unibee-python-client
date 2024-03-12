# UnibeeApiMerchantPlanPlanDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_ids** | **List[int]** | AddonIds | [optional] 
**addons** | [**List[UnibeeApiBeanPlanSimplify]**](UnibeeApiBeanPlanSimplify.md) | Addons | [optional] 
**metric_plan_limits** | [**List[UnibeeApiBeanMerchantMetricPlanLimit]**](UnibeeApiBeanMerchantMetricPlanLimit.md) | MetricPlanLimits | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_plan_detail import UnibeeApiMerchantPlanPlanDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanPlanDetail from a JSON string
unibee_api_merchant_plan_plan_detail_instance = UnibeeApiMerchantPlanPlanDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanPlanDetail.to_json()

# convert the object into a dict
unibee_api_merchant_plan_plan_detail_dict = unibee_api_merchant_plan_plan_detail_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanPlanDetail from a dict
unibee_api_merchant_plan_plan_detail_form_dict = unibee_api_merchant_plan_plan_detail.from_dict(unibee_api_merchant_plan_plan_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


