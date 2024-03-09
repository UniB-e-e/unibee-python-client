# UnibeeInternalQueryEmailTemplateVo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**id** | **int** |  | [optional] 
**merchant_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**template_attach_name** | **str** |  | [optional] 
**template_content** | **str** |  | [optional] 
**template_description** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_title** | **str** |  | [optional] 
**update_time** | **int** | update utc time | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_query_email_template_vo import UnibeeInternalQueryEmailTemplateVo

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalQueryEmailTemplateVo from a JSON string
unibee_internal_query_email_template_vo_instance = UnibeeInternalQueryEmailTemplateVo.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalQueryEmailTemplateVo.to_json()

# convert the object into a dict
unibee_internal_query_email_template_vo_dict = unibee_internal_query_email_template_vo_instance.to_dict()
# create an instance of UnibeeInternalQueryEmailTemplateVo from a dict
unibee_internal_query_email_template_vo_form_dict = unibee_internal_query_email_template_vo.from_dict(unibee_internal_query_email_template_vo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


