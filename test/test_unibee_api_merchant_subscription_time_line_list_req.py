# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_subscription_time_line_list_req import UnibeeApiMerchantSubscriptionTimeLineListReq

class TestUnibeeApiMerchantSubscriptionTimeLineListReq(unittest.TestCase):
    """UnibeeApiMerchantSubscriptionTimeLineListReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantSubscriptionTimeLineListReq:
        """Test UnibeeApiMerchantSubscriptionTimeLineListReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantSubscriptionTimeLineListReq`
        """
        model = UnibeeApiMerchantSubscriptionTimeLineListReq()
        if include_optional:
            return UnibeeApiMerchantSubscriptionTimeLineListReq(
                count = 56,
                page = 56,
                sort_field = '',
                sort_type = '',
                user_id = 56
            )
        else:
            return UnibeeApiMerchantSubscriptionTimeLineListReq(
        )
        """

    def testUnibeeApiMerchantSubscriptionTimeLineListReq(self):
        """Test UnibeeApiMerchantSubscriptionTimeLineListReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()