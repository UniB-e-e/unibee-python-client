# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_profile_update_res import UnibeeApiMerchantProfileUpdateRes

class TestUnibeeApiMerchantProfileUpdateRes(unittest.TestCase):
    """UnibeeApiMerchantProfileUpdateRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantProfileUpdateRes:
        """Test UnibeeApiMerchantProfileUpdateRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantProfileUpdateRes`
        """
        model = UnibeeApiMerchantProfileUpdateRes()
        if include_optional:
            return UnibeeApiMerchantProfileUpdateRes(
                merchant = openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant.unibee.internal.model.entity.oversea_pay.Merchant(
                    address = '', 
                    api_key = '', 
                    business_num = '', 
                    company_id = 56, 
                    company_logo = '', 
                    company_name = '', 
                    create_time = 56, 
                    email = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    home_url = '', 
                    host = '', 
                    id = 56, 
                    idcard = '', 
                    is_deleted = 56, 
                    location = '', 
                    name = '', 
                    phone = '', 
                    time_zone = '', 
                    type = 56, 
                    user_id = 56, )
            )
        else:
            return UnibeeApiMerchantProfileUpdateRes(
        )
        """

    def testUnibeeApiMerchantProfileUpdateRes(self):
        """Test UnibeeApiMerchantProfileUpdateRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
