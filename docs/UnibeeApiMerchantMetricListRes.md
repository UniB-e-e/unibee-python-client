# UnibeeApiMerchantMetricListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_metrics** | [**List[UnibeeApiBeanMerchantMetricSimplify]**](UnibeeApiBeanMerchantMetricSimplify.md) | MerchantMetrics | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_list_res import UnibeeApiMerchantMetricListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricListRes from a JSON string
unibee_api_merchant_metric_list_res_instance = UnibeeApiMerchantMetricListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricListRes.to_json()

# convert the object into a dict
unibee_api_merchant_metric_list_res_dict = unibee_api_merchant_metric_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricListRes from a dict
unibee_api_merchant_metric_list_res_form_dict = unibee_api_merchant_metric_list_res.from_dict(unibee_api_merchant_metric_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


