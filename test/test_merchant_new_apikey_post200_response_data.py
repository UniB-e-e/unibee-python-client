# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_new_apikey_post200_response_data import MerchantNewApikeyPost200ResponseData

class TestMerchantNewApikeyPost200ResponseData(unittest.TestCase):
    """MerchantNewApikeyPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantNewApikeyPost200ResponseData:
        """Test MerchantNewApikeyPost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantNewApikeyPost200ResponseData`
        """
        model = MerchantNewApikeyPost200ResponseData()
        if include_optional:
            return MerchantNewApikeyPost200ResponseData(
                api_key = ''
            )
        else:
            return MerchantNewApikeyPost200ResponseData(
        )
        """

    def testMerchantNewApikeyPost200ResponseData(self):
        """Test MerchantNewApikeyPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()