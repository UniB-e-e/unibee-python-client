# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_invoice_mark_refund_req import UnibeeApiMerchantInvoiceMarkRefundReq

class TestUnibeeApiMerchantInvoiceMarkRefundReq(unittest.TestCase):
    """UnibeeApiMerchantInvoiceMarkRefundReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantInvoiceMarkRefundReq:
        """Test UnibeeApiMerchantInvoiceMarkRefundReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantInvoiceMarkRefundReq`
        """
        model = UnibeeApiMerchantInvoiceMarkRefundReq()
        if include_optional:
            return UnibeeApiMerchantInvoiceMarkRefundReq(
                invoice_id = '',
                reason = '',
                refund_amount = 56,
                refund_no = ''
            )
        else:
            return UnibeeApiMerchantInvoiceMarkRefundReq(
                invoice_id = '',
                reason = '',
                refund_amount = 56,
        )
        """

    def testUnibeeApiMerchantInvoiceMarkRefundReq(self):
        """Test UnibeeApiMerchantInvoiceMarkRefundReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
