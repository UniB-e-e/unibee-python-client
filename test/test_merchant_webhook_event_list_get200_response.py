# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_webhook_event_list_get200_response import MerchantWebhookEventListGet200Response

class TestMerchantWebhookEventListGet200Response(unittest.TestCase):
    """MerchantWebhookEventListGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantWebhookEventListGet200Response:
        """Test MerchantWebhookEventListGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantWebhookEventListGet200Response`
        """
        model = MerchantWebhookEventListGet200Response()
        if include_optional:
            return MerchantWebhookEventListGet200Response(
                code = 56,
                data = openapi_client.models._merchant_webhook_event_list_get_200_response_data._merchant_webhook_event_list_get_200_response_data(
                    event_list = [
                        ''
                        ], ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantWebhookEventListGet200Response(
        )
        """

    def testMerchantWebhookEventListGet200Response(self):
        """Test MerchantWebhookEventListGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
