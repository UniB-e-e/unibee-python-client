# UnibeeApiBeanMerchantEmailTemplateSimplify


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
from openapi_client.models.unibee_api_bean_merchant_email_template_simplify import UnibeeApiBeanMerchantEmailTemplateSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantEmailTemplateSimplify from a JSON string
unibee_api_bean_merchant_email_template_simplify_instance = UnibeeApiBeanMerchantEmailTemplateSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantEmailTemplateSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_email_template_simplify_dict = unibee_api_bean_merchant_email_template_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantEmailTemplateSimplify from a dict
unibee_api_bean_merchant_email_template_simplify_form_dict = unibee_api_bean_merchant_email_template_simplify.from_dict(unibee_api_bean_merchant_email_template_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


