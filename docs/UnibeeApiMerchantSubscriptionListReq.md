# UnibeeApiMerchantSubscriptionListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**page** | **int** | Page, Start WIth 0 | [optional] 
**sort_field** | **str** | Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
**sort_type** | **str** | Sort Type，asc|desc，Default desc | [optional] 
**status** | **List[int]** | Filter, Default All，Status，0-Init | 1-Create｜2-Active｜3-Suspend | 4-Cancel | 5-Expire | [optional] 
**user_id** | **int** | UserId | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_list_req import UnibeeApiMerchantSubscriptionListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionListReq from a JSON string
unibee_api_merchant_subscription_list_req_instance = UnibeeApiMerchantSubscriptionListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionListReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_list_req_dict = unibee_api_merchant_subscription_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionListReq from a dict
unibee_api_merchant_subscription_list_req_form_dict = unibee_api_merchant_subscription_list_req.from_dict(unibee_api_merchant_subscription_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


