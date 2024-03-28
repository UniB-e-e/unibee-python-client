# UnibeeApiMerchantPlanNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_ids** | **List[int]** | Plan Ids Of Recurring Addon Type | [optional] 
**amount** | **int** | Plan CaptureAmount | 
**currency** | **str** | Plan Currency | 
**description** | **str** | Description | [optional] 
**gas_payer** | **str** | who pay the gas for crypto payment, merchant|user | [optional] 
**home_url** | **str** | HomeUrl,Start With: http | [optional] 
**image_url** | **str** | ImageUrl,Start With: http | [optional] 
**interval_count** | **int** | Number Of IntervalUnit，em: day|month|year|week | [optional] 
**interval_unit** | **str** | Plan Interval Unit，em: day|month|year|week | [optional] 
**metadata** | **Dict[str, str]** | Metadata，Map | [optional] 
**metric_limits** | [**List[UnibeeApiBeanBulkMetricLimitPlanBindingParam]**](UnibeeApiBeanBulkMetricLimitPlanBindingParam.md) | Plan&#39;s MetricLimit List | [optional] 
**onetime_addon_ids** | **List[int]** | Plan Ids Of Onetime Addon Type | [optional] 
**plan_name** | **str** | Plan Name | 
**product_description** | **str** | Default Copy Description | [optional] 
**product_name** | **str** | Default Copy PlanName | [optional] 
**type** | **int** | Default 1，,1-main plan，2-addon plan, 3-onetime plan | [optional] [default to 1]

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_new_req import UnibeeApiMerchantPlanNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanNewReq from a JSON string
unibee_api_merchant_plan_new_req_instance = UnibeeApiMerchantPlanNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_plan_new_req_dict = unibee_api_merchant_plan_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanNewReq from a dict
unibee_api_merchant_plan_new_req_form_dict = unibee_api_merchant_plan_new_req.from_dict(unibee_api_merchant_plan_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


