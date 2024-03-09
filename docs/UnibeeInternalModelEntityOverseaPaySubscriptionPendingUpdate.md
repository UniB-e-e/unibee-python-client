# UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_data** | **str** | plan addon data (json) of this period | [optional] 
**amount** | **int** | amount of this period, cent | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency of this period | [optional] 
**data** | **str** |  | [optional] 
**effect_immediate** | **int** | effect immediate，0-no，1-yes | [optional] 
**effect_time** | **int** | effect_immediate&#x3D;0, effect time, utc_time | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_status** | **str** | gateway status | [optional] 
**gmt_create** | **str** | create time | [optional] 
**gmt_modify** | **str** | update time | [optional] 
**id** | **int** | id | [optional] 
**invoice_id** | **str** | gateway update payment id assosiate to this update, use payment.paymentId | [optional] 
**is_deleted** | **int** | 0-UnDeleted，1-Deleted | [optional] 
**link** | **str** | payment link | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**merchant_member_id** | **int** | merchant_user_id | [optional] 
**name** | **str** | name | [optional] 
**note** | **str** | note | [optional] 
**paid** | **int** | paid，0-no，1-yes | [optional] 
**plan_id** | **int** | the plan id of this period | [optional] 
**proration_amount** | **int** | proration amount of this pending update , cent | [optional] 
**proration_date** | **int** | merchant_user_id | [optional] 
**quantity** | **int** | quantity of this period | [optional] 
**response_data** | **str** |  | [optional] 
**status** | **int** | status，0-Init | 1-Create｜2-Finished｜3-Cancelled | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**update_addon_data** | **str** | plan addon data (json) after update | [optional] 
**update_amount** | **int** | the amount after update | [optional] 
**update_currency** | **str** | the currency after update | [optional] 
**update_plan_id** | **int** | the plan id after update | [optional] 
**update_quantity** | **int** | quantity after update | [optional] 
**update_subscription_id** | **str** | pending update unique id | [optional] 
**user_id** | **int** | userId | [optional] 

## Example

```python
from openapi_client.models.unibee_internal_model_entity_oversea_pay_subscription_pending_update import UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate from a JSON string
unibee_internal_model_entity_oversea_pay_subscription_pending_update_instance = UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate.from_json(json)
# print the JSON string representation of the object
print UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate.to_json()

# convert the object into a dict
unibee_internal_model_entity_oversea_pay_subscription_pending_update_dict = unibee_internal_model_entity_oversea_pay_subscription_pending_update_instance.to_dict()
# create an instance of UnibeeInternalModelEntityOverseaPaySubscriptionPendingUpdate from a dict
unibee_internal_model_entity_oversea_pay_subscription_pending_update_form_dict = unibee_internal_model_entity_oversea_pay_subscription_pending_update.from_dict(unibee_internal_model_entity_oversea_pay_subscription_pending_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


