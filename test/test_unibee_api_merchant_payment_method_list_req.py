# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_payment_method_list_req import UnibeeApiMerchantPaymentMethodListReq

class TestUnibeeApiMerchantPaymentMethodListReq(unittest.TestCase):
    """UnibeeApiMerchantPaymentMethodListReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantPaymentMethodListReq:
        """Test UnibeeApiMerchantPaymentMethodListReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantPaymentMethodListReq`
        """
        model = UnibeeApiMerchantPaymentMethodListReq()
        if include_optional:
            return UnibeeApiMerchantPaymentMethodListReq(
                gateway_id = 56,
                payment_id = '',
                user_id = 56
            )
        else:
            return UnibeeApiMerchantPaymentMethodListReq(
                gateway_id = 56,
        )
        """

    def testUnibeeApiMerchantPaymentMethodListReq(self):
        """Test UnibeeApiMerchantPaymentMethodListReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
