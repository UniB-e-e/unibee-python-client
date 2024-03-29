# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_logic_gateway_ro_refund_simplify import UnibeeInternalLogicGatewayRoRefundSimplify

class TestUnibeeInternalLogicGatewayRoRefundSimplify(unittest.TestCase):
    """UnibeeInternalLogicGatewayRoRefundSimplify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalLogicGatewayRoRefundSimplify:
        """Test UnibeeInternalLogicGatewayRoRefundSimplify
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalLogicGatewayRoRefundSimplify`
        """
        model = UnibeeInternalLogicGatewayRoRefundSimplify()
        if include_optional:
            return UnibeeInternalLogicGatewayRoRefundSimplify(
                country_code = '',
                create_time = 56,
                currency = '',
                external_refund_id = '',
                gateway_id = 56,
                gateway_refund_id = '',
                merchant_id = 56,
                payment_id = '',
                refund_amount = 56,
                refund_comment = '',
                refund_id = '',
                refund_time = 56,
                return_url = '',
                status = 56,
                subscription_id = '',
                user_id = 56
            )
        else:
            return UnibeeInternalLogicGatewayRoRefundSimplify(
        )
        """

    def testUnibeeInternalLogicGatewayRoRefundSimplify(self):
        """Test UnibeeInternalLogicGatewayRoRefundSimplify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
