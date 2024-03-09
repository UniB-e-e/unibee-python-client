# UnibeeApiMerchantPaymentTimeLineListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count Of Page | [optional] 
**page** | **int** | Page,Start 0 | [optional] 
**sort_field** | **str** | Sort，invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify | [optional] 
**sort_type** | **str** | Sort Type，asc|desc，Default desc | [optional] 
**user_id** | **int** | Filter UserId, Default All | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_time_line_list_req import UnibeeApiMerchantPaymentTimeLineListReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentTimeLineListReq from a JSON string
unibee_api_merchant_payment_time_line_list_req_instance = UnibeeApiMerchantPaymentTimeLineListReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentTimeLineListReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_time_line_list_req_dict = unibee_api_merchant_payment_time_line_list_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentTimeLineListReq from a dict
unibee_api_merchant_payment_time_line_list_req_form_dict = unibee_api_merchant_payment_time_line_list_req.from_dict(unibee_api_merchant_payment_time_line_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


