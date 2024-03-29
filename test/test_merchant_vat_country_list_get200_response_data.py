# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_vat_country_list_get200_response_data import MerchantVatCountryListGet200ResponseData

class TestMerchantVatCountryListGet200ResponseData(unittest.TestCase):
    """MerchantVatCountryListGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantVatCountryListGet200ResponseData:
        """Test MerchantVatCountryListGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantVatCountryListGet200ResponseData`
        """
        model = MerchantVatCountryListGet200ResponseData()
        if include_optional:
            return MerchantVatCountryListGet200ResponseData(
                vat_country_list = [
                    openapi_client.models.unibee/internal/logic/gateway/ro/vat_country_rate.unibee.internal.logic.gateway.ro.VatCountryRate(
                        country_code = '', 
                        country_name = '', 
                        gateway = '', 
                        id = 56, 
                        standard_tax_percentage = 56, 
                        vat_support = True, )
                    ]
            )
        else:
            return MerchantVatCountryListGet200ResponseData(
        )
        """

    def testMerchantVatCountryListGet200ResponseData(self):
        """Test MerchantVatCountryListGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
