# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_email_template_deactivate_req import UnibeeApiMerchantEmailTemplateDeactivateReq

class TestUnibeeApiMerchantEmailTemplateDeactivateReq(unittest.TestCase):
    """UnibeeApiMerchantEmailTemplateDeactivateReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantEmailTemplateDeactivateReq:
        """Test UnibeeApiMerchantEmailTemplateDeactivateReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantEmailTemplateDeactivateReq`
        """
        model = UnibeeApiMerchantEmailTemplateDeactivateReq()
        if include_optional:
            return UnibeeApiMerchantEmailTemplateDeactivateReq(
                template_name = ''
            )
        else:
            return UnibeeApiMerchantEmailTemplateDeactivateReq(
                template_name = '',
        )
        """

    def testUnibeeApiMerchantEmailTemplateDeactivateReq(self):
        """Test UnibeeApiMerchantEmailTemplateDeactivateReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()