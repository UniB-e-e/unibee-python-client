# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_payment_new_post200_response import MerchantPaymentNewPost200Response

class TestMerchantPaymentNewPost200Response(unittest.TestCase):
    """MerchantPaymentNewPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantPaymentNewPost200Response:
        """Test MerchantPaymentNewPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantPaymentNewPost200Response`
        """
        model = MerchantPaymentNewPost200Response()
        if include_optional:
            return MerchantPaymentNewPost200Response(
                code = 56,
                data = openapi_client.models._merchant_payment_new_post_200_response_data._merchant_payment_new_post_200_response_data(
                    action = openapi_client.models.github/com/gogf/gf/v2/encoding/gjson/json.github.com.gogf.gf.v2.encoding.gjson.Json(), 
                    external_payment_id = '', 
                    payment_id = '', 
                    status = 56, ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantPaymentNewPost200Response(
        )
        """

    def testMerchantPaymentNewPost200Response(self):
        """Test MerchantPaymentNewPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()