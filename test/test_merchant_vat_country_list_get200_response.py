# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_vat_country_list_get200_response import MerchantVatCountryListGet200Response

class TestMerchantVatCountryListGet200Response(unittest.TestCase):
    """MerchantVatCountryListGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantVatCountryListGet200Response:
        """Test MerchantVatCountryListGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantVatCountryListGet200Response`
        """
        model = MerchantVatCountryListGet200Response()
        if include_optional:
            return MerchantVatCountryListGet200Response(
                code = 56,
                data = openapi_client.models._merchant_vat_country_list_get_200_response_data._merchant_vat_country_list_get_200_response_data(
                    vat_country_list = [
                        openapi_client.models.unibee/internal/logic/gateway/ro/vat_country_rate.unibee.internal.logic.gateway.ro.VatCountryRate(
                            country_code = '', 
                            country_name = '', 
                            gateway = '', 
                            id = 56, 
                            standard_tax_percentage = 56, 
                            vat_support = True, )
                        ], ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantVatCountryListGet200Response(
        )
        """

    def testMerchantVatCountryListGet200Response(self):
        """Test MerchantVatCountryListGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
