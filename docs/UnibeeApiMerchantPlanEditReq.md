# UnibeeApiMerchantPlanEditReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_ids** | **List[int]** | Plan Ids Of Addon Type | [optional] 
**amount** | **int** | Plan CaptureAmount | 
**currency** | **str** | Plan Currency | 
**description** | **str** | Description | [optional] 
**home_url** | **str** | HomeUrl,Start With: http | [optional] 
**image_url** | **str** | ImageUrl,Start With: http | [optional] 
**interval_count** | **int** | Default 1，Number Of IntervalUnit | [optional] [default to 1]
**interval_unit** | **str** | Plan Interval Unit，em: day|month|year|week | 
**metric_limits** | [**List[UnibeeInternalLogicGatewayRoBulkMetricLimitPlanBindingParam]**](UnibeeInternalLogicGatewayRoBulkMetricLimitPlanBindingParam.md) | Plan&#39;s MetricLimit List | [optional] 
**plan_id** | **int** | PlanId | 
**plan_name** | **str** | Plan Name | 
**product_description** | **str** | Default Copy Description | [optional] 
**product_name** | **str** | Default Copy PlanName | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_edit_req import UnibeeApiMerchantPlanEditReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanEditReq from a JSON string
unibee_api_merchant_plan_edit_req_instance = UnibeeApiMerchantPlanEditReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanEditReq.to_json()

# convert the object into a dict
unibee_api_merchant_plan_edit_req_dict = unibee_api_merchant_plan_edit_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanEditReq from a dict
unibee_api_merchant_plan_edit_req_form_dict = unibee_api_merchant_plan_edit_req.from_dict(unibee_api_merchant_plan_edit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


