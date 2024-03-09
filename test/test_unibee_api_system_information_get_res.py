# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_system_information_get_res import UnibeeApiSystemInformationGetRes

class TestUnibeeApiSystemInformationGetRes(unittest.TestCase):
    """UnibeeApiSystemInformationGetRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiSystemInformationGetRes:
        """Test UnibeeApiSystemInformationGetRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiSystemInformationGetRes`
        """
        model = UnibeeApiSystemInformationGetRes()
        if include_optional:
            return UnibeeApiSystemInformationGetRes(
                env = '',
                gateway = [
                    openapi_client.models.unibee/internal/logic/gateway/ro/gateway_simplify.unibee.internal.logic.gateway.ro.GatewaySimplify(
                        gateway_id = 56, 
                        gateway_logo = '', 
                        gateway_name = '', )
                    ],
                is_prod = True,
                support_currency = [
                    openapi_client.models.unibee/api/system/information/support_currency.unibee.api.system.information.SupportCurrency(
                        currency = '', 
                        scale = 56, 
                        symbol = '', )
                    ],
                support_time_zone = [
                    ''
                    ]
            )
        else:
            return UnibeeApiSystemInformationGetRes(
        )
        """

    def testUnibeeApiSystemInformationGetRes(self):
        """Test UnibeeApiSystemInformationGetRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()