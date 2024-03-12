# UnibeeApiBeanPaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_payment_method import UnibeeApiBeanPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanPaymentMethod from a JSON string
unibee_api_bean_payment_method_instance = UnibeeApiBeanPaymentMethod.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanPaymentMethod.to_json()

# convert the object into a dict
unibee_api_bean_payment_method_dict = unibee_api_bean_payment_method_instance.to_dict()
# create an instance of UnibeeApiBeanPaymentMethod from a dict
unibee_api_bean_payment_method_form_dict = unibee_api_bean_payment_method.from_dict(unibee_api_bean_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


