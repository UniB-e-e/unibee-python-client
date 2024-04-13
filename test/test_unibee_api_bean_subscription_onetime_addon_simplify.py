# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_bean_subscription_onetime_addon_simplify import UnibeeApiBeanSubscriptionOnetimeAddonSimplify

class TestUnibeeApiBeanSubscriptionOnetimeAddonSimplify(unittest.TestCase):
    """UnibeeApiBeanSubscriptionOnetimeAddonSimplify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiBeanSubscriptionOnetimeAddonSimplify:
        """Test UnibeeApiBeanSubscriptionOnetimeAddonSimplify
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiBeanSubscriptionOnetimeAddonSimplify`
        """
        model = UnibeeApiBeanSubscriptionOnetimeAddonSimplify()
        if include_optional:
            return UnibeeApiBeanSubscriptionOnetimeAddonSimplify(
                addon_id = 56,
                create_time = 56,
                id = 56,
                is_deleted = 56,
                metadata = {
                    'key' : ''
                    },
                payment_id = '',
                payment_link = '',
                quantity = 56,
                status = 56,
                subscription_id = ''
            )
        else:
            return UnibeeApiBeanSubscriptionOnetimeAddonSimplify(
        )
        """

    def testUnibeeApiBeanSubscriptionOnetimeAddonSimplify(self):
        """Test UnibeeApiBeanSubscriptionOnetimeAddonSimplify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()