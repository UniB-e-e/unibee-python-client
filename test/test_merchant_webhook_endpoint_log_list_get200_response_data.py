# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_webhook_endpoint_log_list_get200_response_data import MerchantWebhookEndpointLogListGet200ResponseData

class TestMerchantWebhookEndpointLogListGet200ResponseData(unittest.TestCase):
    """MerchantWebhookEndpointLogListGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantWebhookEndpointLogListGet200ResponseData:
        """Test MerchantWebhookEndpointLogListGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantWebhookEndpointLogListGet200ResponseData`
        """
        model = MerchantWebhookEndpointLogListGet200ResponseData()
        if include_optional:
            return MerchantWebhookEndpointLogListGet200ResponseData(
                endpoint_log_list = [
                    openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant_webhook_log.unibee.internal.model.entity.oversea_pay.MerchantWebhookLog(
                        body = '', 
                        create_time = 56, 
                        endpoint_id = 56, 
                        gmt_create = '', 
                        gmt_modify = '', 
                        id = 56, 
                        mamo = '', 
                        merchant_id = 56, 
                        reconsume_count = 56, 
                        request_id = '', 
                        response = '', 
                        webhook_event = '', 
                        webhook_url = '', )
                    ]
            )
        else:
            return MerchantWebhookEndpointLogListGet200ResponseData(
        )
        """

    def testMerchantWebhookEndpointLogListGet200ResponseData(self):
        """Test MerchantWebhookEndpointLogListGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()