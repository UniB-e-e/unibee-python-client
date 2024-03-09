# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_subscription_admin_note_list_get200_response_data import MerchantSubscriptionAdminNoteListGet200ResponseData

class TestMerchantSubscriptionAdminNoteListGet200ResponseData(unittest.TestCase):
    """MerchantSubscriptionAdminNoteListGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSubscriptionAdminNoteListGet200ResponseData:
        """Test MerchantSubscriptionAdminNoteListGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSubscriptionAdminNoteListGet200ResponseData`
        """
        model = MerchantSubscriptionAdminNoteListGet200ResponseData()
        if include_optional:
            return MerchantSubscriptionAdminNoteListGet200ResponseData(
                note_lists = [
                    openapi_client.models.unibee/api/merchant/subscription/admin_note_ro.unibee.api.merchant.subscription.AdminNoteRo(
                        create_time = 56, 
                        email = '', 
                        first_name = '', 
                        id = 56, 
                        last_name = '', 
                        mobile = '', 
                        note = '', 
                        subscription_id = '', 
                        user_name = '', )
                    ]
            )
        else:
            return MerchantSubscriptionAdminNoteListGet200ResponseData(
        )
        """

    def testMerchantSubscriptionAdminNoteListGet200ResponseData(self):
        """Test MerchantSubscriptionAdminNoteListGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()