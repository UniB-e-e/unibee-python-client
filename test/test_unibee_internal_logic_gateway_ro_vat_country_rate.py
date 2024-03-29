# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_logic_gateway_ro_vat_country_rate import UnibeeInternalLogicGatewayRoVatCountryRate

class TestUnibeeInternalLogicGatewayRoVatCountryRate(unittest.TestCase):
    """UnibeeInternalLogicGatewayRoVatCountryRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalLogicGatewayRoVatCountryRate:
        """Test UnibeeInternalLogicGatewayRoVatCountryRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalLogicGatewayRoVatCountryRate`
        """
        model = UnibeeInternalLogicGatewayRoVatCountryRate()
        if include_optional:
            return UnibeeInternalLogicGatewayRoVatCountryRate(
                country_code = '',
                country_name = '',
                gateway = '',
                id = 56,
                standard_tax_percentage = 56,
                vat_support = True
            )
        else:
            return UnibeeInternalLogicGatewayRoVatCountryRate(
        )
        """

    def testUnibeeInternalLogicGatewayRoVatCountryRate(self):
        """Test UnibeeInternalLogicGatewayRoVatCountryRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
