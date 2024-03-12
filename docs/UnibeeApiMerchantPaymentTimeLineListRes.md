# UnibeeApiMerchantPaymentTimeLineListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_time_lines** | [**List[UnibeeApiBeanPaymentTimelineSimplify]**](UnibeeApiBeanPaymentTimelineSimplify.md) | PaymentTimeLines | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_time_line_list_res import UnibeeApiMerchantPaymentTimeLineListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentTimeLineListRes from a JSON string
unibee_api_merchant_payment_time_line_list_res_instance = UnibeeApiMerchantPaymentTimeLineListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentTimeLineListRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_time_line_list_res_dict = unibee_api_merchant_payment_time_line_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentTimeLineListRes from a dict
unibee_api_merchant_payment_time_line_list_res_form_dict = unibee_api_merchant_payment_time_line_list_res.from_dict(unibee_api_merchant_payment_time_line_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


