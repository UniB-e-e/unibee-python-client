# UnibeeApiBeanGatewaySimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **int** |  | [optional] 
**gateway_logo** | **str** |  | [optional] 
**gateway_name** | **str** |  | [optional] 
**gateway_type** | **int** | gateway type，1-Default｜ 2-Crypto | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_gateway_simplify import UnibeeApiBeanGatewaySimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanGatewaySimplify from a JSON string
unibee_api_bean_gateway_simplify_instance = UnibeeApiBeanGatewaySimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanGatewaySimplify.to_json()

# convert the object into a dict
unibee_api_bean_gateway_simplify_dict = unibee_api_bean_gateway_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanGatewaySimplify from a dict
unibee_api_bean_gateway_simplify_form_dict = unibee_api_bean_gateway_simplify.from_dict(unibee_api_bean_gateway_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


