# UnibeeApiSystemInformationGetRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | **str** | System Env, em: daily|stage|local|prod | [optional] 
**gateway** | [**List[UnibeeInternalLogicGatewayRoGatewaySimplify]**](UnibeeInternalLogicGatewayRoGatewaySimplify.md) | Support Currency List | [optional] 
**is_prod** | **bool** | Check System Env Is Prod, true|false | [optional] 
**support_currency** | [**List[UnibeeApiSystemInformationSupportCurrency]**](UnibeeApiSystemInformationSupportCurrency.md) | Support Currency List | [optional] 
**support_time_zone** | **List[str]** | Support TimeZone List | [optional] 

## Example

```python
from openapi_client.models.unibee_api_system_information_get_res import UnibeeApiSystemInformationGetRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiSystemInformationGetRes from a JSON string
unibee_api_system_information_get_res_instance = UnibeeApiSystemInformationGetRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiSystemInformationGetRes.to_json()

# convert the object into a dict
unibee_api_system_information_get_res_dict = unibee_api_system_information_get_res_instance.to_dict()
# create an instance of UnibeeApiSystemInformationGetRes from a dict
unibee_api_system_information_get_res_form_dict = unibee_api_system_information_get_res.from_dict(unibee_api_system_information_get_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


