# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_gateway_setup_webhook_post200_response import MerchantGatewaySetupWebhookPost200Response

class TestMerchantGatewaySetupWebhookPost200Response(unittest.TestCase):
    """MerchantGatewaySetupWebhookPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantGatewaySetupWebhookPost200Response:
        """Test MerchantGatewaySetupWebhookPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantGatewaySetupWebhookPost200Response`
        """
        model = MerchantGatewaySetupWebhookPost200Response()
        if include_optional:
            return MerchantGatewaySetupWebhookPost200Response(
                code = 56,
                data = openapi_client.models._merchant_gateway_setup_webhook_post_200_response_data._merchant_gateway_setup_webhook_post_200_response_data(
                    gateway_webhook_url = '', ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantGatewaySetupWebhookPost200Response(
        )
        """

    def testMerchantGatewaySetupWebhookPost200Response(self):
        """Test MerchantGatewaySetupWebhookPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
