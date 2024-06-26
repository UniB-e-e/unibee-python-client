# MerchantGetGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**List[UnibeeApiBeanCurrency]**](UnibeeApiBeanCurrency.md) | Currency List | [optional] 
**time_zone** | **List[str]** | TimeZone List | [optional] 
**env** | **str** | System Env, em: daily|stage|local|prod | [optional] 
**gateway** | [**List[UnibeeApiBeanGatewaySimplify]**](UnibeeApiBeanGatewaySimplify.md) | Gateway List | [optional] 
**is_prod** | **bool** | Check System Env Is Prod, true|false | [optional] 
**merchant** | [**UnibeeApiBeanMerchantSimplify**](UnibeeApiBeanMerchantSimplify.md) |  | [optional] 
**merchant_member** | [**UnibeeApiBeanDetailMerchantMemberDetail**](UnibeeApiBeanDetailMerchantMemberDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.merchant_get_get200_response_data import MerchantGetGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGetGet200ResponseData from a JSON string
merchant_get_get200_response_data_instance = MerchantGetGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantGetGet200ResponseData.to_json()

# convert the object into a dict
merchant_get_get200_response_data_dict = merchant_get_get200_response_data_instance.to_dict()
# create an instance of MerchantGetGet200ResponseData from a dict
merchant_get_get200_response_data_form_dict = merchant_get_get200_response_data.from_dict(merchant_get_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


