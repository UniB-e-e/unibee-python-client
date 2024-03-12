# UnibeeApiMerchantMetricUserMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) | Addon | [optional] 
**is_paid** | **bool** | IsPaid | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**subscription** | [**UnibeeApiBeanSubscriptionSimplify**](UnibeeApiBeanSubscriptionSimplify.md) |  | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 
**user_merchant_metric_stats** | [**List[UnibeeApiBeanUserMerchantMetricStat]**](UnibeeApiBeanUserMerchantMetricStat.md) | UserMerchantMetricStats | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_metric_user_metric import UnibeeApiMerchantMetricUserMetric

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantMetricUserMetric from a JSON string
unibee_api_merchant_metric_user_metric_instance = UnibeeApiMerchantMetricUserMetric.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantMetricUserMetric.to_json()

# convert the object into a dict
unibee_api_merchant_metric_user_metric_dict = unibee_api_merchant_metric_user_metric_instance.to_dict()
# create an instance of UnibeeApiMerchantMetricUserMetric from a dict
unibee_api_merchant_metric_user_metric_form_dict = unibee_api_merchant_metric_user_metric.from_dict(unibee_api_merchant_metric_user_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


