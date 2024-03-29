# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_country_config_list_post200_response import MerchantCountryConfigListPost200Response

class TestMerchantCountryConfigListPost200Response(unittest.TestCase):
    """MerchantCountryConfigListPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantCountryConfigListPost200Response:
        """Test MerchantCountryConfigListPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantCountryConfigListPost200Response`
        """
        model = MerchantCountryConfigListPost200Response()
        if include_optional:
            return MerchantCountryConfigListPost200Response(
                code = 56,
                data = openapi_client.models._merchant_country_config_list_post_200_response_data._merchant_country_config_list_post_200_response_data(
                    configs = [
                        openapi_client.models.unibee/api/bean/merchant_country_config_simplify.unibee.api.bean.MerchantCountryConfigSimplify(
                            country_code = '', 
                            merchant_id = 56, 
                            name = '', )
                        ], ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantCountryConfigListPost200Response(
        )
        """

    def testMerchantCountryConfigListPost200Response(self):
        """Test MerchantCountryConfigListPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
