# MerchantPlanListGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**List[UnibeeApiMerchantPlanPlanDetail]**](UnibeeApiMerchantPlanPlanDetail.md) | Plans | [optional] 

## Example

```python
from openapi_client.models.merchant_plan_list_get200_response_data import MerchantPlanListGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantPlanListGet200ResponseData from a JSON string
merchant_plan_list_get200_response_data_instance = MerchantPlanListGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantPlanListGet200ResponseData.to_json()

# convert the object into a dict
merchant_plan_list_get200_response_data_dict = merchant_plan_list_get200_response_data_instance.to_dict()
# create an instance of MerchantPlanListGet200ResponseData from a dict
merchant_plan_list_get200_response_data_form_dict = merchant_plan_list_get200_response_data.from_dict(merchant_plan_list_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


