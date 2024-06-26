# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_member_list_get200_response_data import MerchantMemberListGet200ResponseData

class TestMerchantMemberListGet200ResponseData(unittest.TestCase):
    """MerchantMemberListGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantMemberListGet200ResponseData:
        """Test MerchantMemberListGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantMemberListGet200ResponseData`
        """
        model = MerchantMemberListGet200ResponseData()
        if include_optional:
            return MerchantMemberListGet200ResponseData(
                merchant_members = [
                    openapi_client.models.unibee/api/bean/merchant_member_simplify.unibee.api.bean.MerchantMemberSimplify(
                        create_time = 56, 
                        email = '', 
                        first_name = '', 
                        id = 56, 
                        last_name = '', 
                        merchant_id = 56, 
                        mobile = '', 
                        role = '', )
                    ]
            )
        else:
            return MerchantMemberListGet200ResponseData(
        )
        """

    def testMerchantMemberListGet200ResponseData(self):
        """Test MerchantMemberListGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
