# UnibeeInternalModelEntityOverseaPayPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | amount, cent, without tax | [optional] 
**binding_addon_ids** | **str** | binded addon planIds，split with , | [optional] 
**company_id** | **int** | company id | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**description** | **str** | description | [optional] 
**extra_metric_data** | **str** |  | [optional] 
**gateway_product_description** | **str** | gateway product description | [optional] 
**gateway_product_name** | **str** | gateway product name | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**home_url** | **str** | home_url | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** | image_url | [optional] 
**interval_count** | **int** | period unit count | [optional] 
**interval_unit** | **str** | period unit,day|month|year|week | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**plan_name** | **str** | PlanName | [optional] 
**publish_status** | **int** | 1-UnPublish,2-Publish, Use For Display Plan At UserPortal | [optional] 
**status** | **int** | status，1-editing，2-active，3-inactive，4-expired | [optional] 
**tax_inclusive** | **int** | deperated | [optional] 
**tax_scale** | **int** | tax scale 1000 &#x3D; 10% | [optional] 
**type** | **int** | type，1-main plan，2-addon plan | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_plan import UnibeeInternalModelEntityOverseaPayPlan

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPayPlan from a JSON string
unibee_internal_model_entity_oversea_pay_plan_instance = UnibeeInternalModelEntityOverseaPayPlan.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPayPlan.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_plan_dict = unibee_internal_model_entity_oversea_pay_plan_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPayPlan from a dict
unibee_internal_model_entity_oversea_pay_plan_form_dict = unibee_internal_model_entity_oversea_pay_plan.from_dict(unibee_internal_model_entity_oversea_pay_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


