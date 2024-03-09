# UnibeeApiMerchantPlanListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Per Page | [optional] 
**currency** | **str** | Filter Currency | [optional] 
**page** | **int** | Page, Start 0 | [optional] 
**publish_status** | **int** | Filter, Default All，PublishStatus，1-UnPublished，2-Published | [optional] 
**sort_field** | **str** | Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
**sort_type** | **str** | Sort Type，asc|desc，Default desc | [optional] 
**status** | **List[int]** | Filter, Default All，,Status，1-Editing，2-Active，3-InActive，4-Expired | [optional] 
**type** | **List[int]** | 1-main plan，2-addon plan | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_list_req import UnibeeApiMerchantPlanListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanListReq from a JSON string
unibee_api_merchant_plan_list_req_instance = UnibeeApiMerchantPlanListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanListReq.to_json()

# convert the object into a dict
unibee_api_merchant_plan_list_req_dict = unibee_api_merchant_plan_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanListReq from a dict
unibee_api_merchant_plan_list_req_form_dict = unibee_api_merchant_plan_list_req.from_dict(unibee_api_merchant_plan_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


