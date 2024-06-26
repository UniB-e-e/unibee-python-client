# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_role_list_res import UnibeeApiMerchantRoleListRes

class TestUnibeeApiMerchantRoleListRes(unittest.TestCase):
    """UnibeeApiMerchantRoleListRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantRoleListRes:
        """Test UnibeeApiMerchantRoleListRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantRoleListRes`
        """
        model = UnibeeApiMerchantRoleListRes()
        if include_optional:
            return UnibeeApiMerchantRoleListRes(
                merchant_roles = [
                    openapi_client.models.unibee/api/bean/merchant_role_simplify.unibee.api.bean.MerchantRoleSimplify(
                        create_time = 56, 
                        id = 56, 
                        merchant_id = 56, 
                        permissions = [
                            openapi_client.models.unibee/api/bean/merchant_role_permission.unibee.api.bean.MerchantRolePermission(
                                group = '', )
                            ], 
                        role = '', )
                    ]
            )
        else:
            return UnibeeApiMerchantRoleListRes(
        )
        """

    def testUnibeeApiMerchantRoleListRes(self):
        """Test UnibeeApiMerchantRoleListRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
