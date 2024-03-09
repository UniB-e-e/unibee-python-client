# UnibeeInternalModelEntityOverseaPaySubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_data** | **str** | plan addon json data | [optional] 
**amount** | **int** | amount, cent | [optional] 
**billing_cycle_anchor** | **int** | billing_cycle_anchor | [optional] 
**cancel_at_period_end** | **int** | whether cancel at period end，0-false | 1-true | [optional] 
**cancel_reason** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**current_period_end** | **int** | current_period_end, utc time | [optional] 
**current_period_end_time** | **str** |  | [optional] 
**current_period_start** | **int** | current_period_start, utc time | [optional] 
**current_period_start_time** | **str** |  | [optional] 
**customer_email** | **str** | customer_email | [optional] 
**customer_name** | **str** | customer_name | [optional] 
**data** | **str** |  | [optional] 
**dunning_time** | **int** | dunning_time, utc time | [optional] 
**first_paid_time** | **int** | first success payment time | [optional] 
**gateway_default_payment_method** | **str** |  | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_item_data** | **str** | gateway_item_data | [optional] 
**gateway_latest_invoice_id** | **str** | gateway latest invoice id | [optional] 
**gateway_status** | **str** | gateway status，Stripe：https://stripe.com/docs/billing/subscriptions/webhooks  Paypal：https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_get | [optional] 
**gateway_subscription_id** | **str** | gateway subscription id | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**id** | **int** |  | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**last_update_time** | **int** |  | [optional] 
**latest_invoice_id** | **str** | latest_invoice_id | [optional] 
**link** | **str** |  | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**pending_update_id** | **str** |  | [optional] 
**plan_id** | **int** | plan id | [optional] 
**quantity** | **int** | quantity | [optional] 
**response_data** | **str** |  | [optional] 
**return_url** | **str** |  | [optional] 
**status** | **int** | status，0-Init | 1-Create｜2-Active｜3-PendingInActive | 4-Cancel | 5-Expire | 6- Suspend| 7-Incomplete | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**task_time** | **str** | task_time | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**test_clock** | **int** | test_clock, simulator clock for subscription, if set , sub will out of cronjob controll | [optional] 
**trial_end** | **int** | trial_end, utc time | [optional] 
**type** | **int** | sub type, 0-gateway sub, 1-unibee sub | [optional] 
**user_id** | **int** | userId | [optional] 
**vat_number** | **str** |  | [optional] 
**vat_verify_data** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_subscription import UnibeeInternalModelEntityOverseaPaySubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPaySubscription from a JSON string
unibee_internal_model_entity_oversea_pay_subscription_instance = UnibeeInternalModelEntityOverseaPaySubscription.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPaySubscription.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_subscription_dict = unibee_internal_model_entity_oversea_pay_subscription_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPaySubscription from a dict
unibee_internal_model_entity_oversea_pay_subscription_form_dict = unibee_internal_model_entity_oversea_pay_subscription.from_dict(unibee_internal_model_entity_oversea_pay_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


