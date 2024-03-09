# UnibeeApiMerchantAuthLoginOtpVerifyReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | 
**verification_code** | **str** | VerificationCode | 

## Example

```python
from openapi_client.models.unibee_api_merchant_auth_login_otp_verify_req import UnibeeApiMerchantAuthLoginOtpVerifyReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantAuthLoginOtpVerifyReq from a JSON string
unibee_api_merchant_auth_login_otp_verify_req_instance = UnibeeApiMerchantAuthLoginOtpVerifyReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantAuthLoginOtpVerifyReq.to_json()

# convert the object into a dict
unibee_api_merchant_auth_login_otp_verify_req_dict = unibee_api_merchant_auth_login_otp_verify_req_instance.to_dict()
# create an instance of UnibeeApiMerchantAuthLoginOtpVerifyReq from a dict
unibee_api_merchant_auth_login_otp_verify_req_form_dict = unibee_api_merchant_auth_login_otp_verify_req.from_dict(unibee_api_merchant_auth_login_otp_verify_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


