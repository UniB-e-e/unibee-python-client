# UnibeeApiMerchantEmailTemplateUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_content** | **str** | templateContent | 
**template_name** | **str** | templateName | 
**template_title** | **str** | templateTitle | 

## Example

```python
from openapi_client.models.unibee_api_merchant_email_template_update_req import UnibeeApiMerchantEmailTemplateUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantEmailTemplateUpdateReq from a JSON string
unibee_api_merchant_email_template_update_req_instance = UnibeeApiMerchantEmailTemplateUpdateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantEmailTemplateUpdateReq.to_json()

# convert the object into a dict
unibee_api_merchant_email_template_update_req_dict = unibee_api_merchant_email_template_update_req_instance.to_dict()
# create an instance of UnibeeApiMerchantEmailTemplateUpdateReq from a dict
unibee_api_merchant_email_template_update_req_form_dict = unibee_api_merchant_email_template_update_req.from_dict(unibee_api_merchant_email_template_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


