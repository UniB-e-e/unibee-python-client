# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_auth_sso_login_post200_response_data import MerchantAuthSsoLoginPost200ResponseData

class TestMerchantAuthSsoLoginPost200ResponseData(unittest.TestCase):
    """MerchantAuthSsoLoginPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantAuthSsoLoginPost200ResponseData:
        """Test MerchantAuthSsoLoginPost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantAuthSsoLoginPost200ResponseData`
        """
        model = MerchantAuthSsoLoginPost200ResponseData()
        if include_optional:
            return MerchantAuthSsoLoginPost200ResponseData(
                merchant_member = openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant_member.unibee.internal.model.entity.oversea_pay.MerchantMember(
                    create_time = 56, 
                    email = '', 
                    first_name = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    id = 56, 
                    is_deleted = 56, 
                    last_name = '', 
                    merchant_id = 56, 
                    mobile = '', 
                    password = '', 
                    user_name = '', ),
                token = ''
            )
        else:
            return MerchantAuthSsoLoginPost200ResponseData(
        )
        """

    def testMerchantAuthSsoLoginPost200ResponseData(self):
        """Test MerchantAuthSsoLoginPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()