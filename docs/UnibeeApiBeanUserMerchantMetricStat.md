# UnibeeApiBeanUserMerchantMetricStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_use_value** | **int** |  | [optional] 
**metric_limit** | [**UnibeeApiBeanPlanMetricLimitDetail**](UnibeeApiBeanPlanMetricLimitDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_user_merchant_metric_stat import UnibeeApiBeanUserMerchantMetricStat

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanUserMerchantMetricStat from a JSON string
unibee_api_bean_user_merchant_metric_stat_instance = UnibeeApiBeanUserMerchantMetricStat.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanUserMerchantMetricStat.to_json()

# convert the object into a dict
unibee_api_bean_user_merchant_metric_stat_dict = unibee_api_bean_user_merchant_metric_stat_instance.to_dict()
# create an instance of UnibeeApiBeanUserMerchantMetricStat from a dict
unibee_api_bean_user_merchant_metric_stat_form_dict = unibee_api_bean_user_merchant_metric_stat.from_dict(unibee_api_bean_user_merchant_metric_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


