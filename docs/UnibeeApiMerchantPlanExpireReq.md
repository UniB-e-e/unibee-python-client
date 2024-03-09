# UnibeeApiMerchantPlanExpireReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_code** | **int** | Code From Email | 
**plan_id** | **int** | PlanId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_plan_expire_req import UnibeeApiMerchantPlanExpireReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPlanExpireReq from a JSON string
unibee_api_merchant_plan_expire_req_instance = UnibeeApiMerchantPlanExpireReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPlanExpireReq.to_json()

# convert the object into a dict
unibee_api_merchant_plan_expire_req_dict = unibee_api_merchant_plan_expire_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPlanExpireReq from a dict
unibee_api_merchant_plan_expire_req_form_dict = unibee_api_merchant_plan_expire_req.from_dict(unibee_api_merchant_plan_expire_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


