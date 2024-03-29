# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_invoice_mark_refund_post200_response_data import MerchantInvoiceMarkRefundPost200ResponseData

class TestMerchantInvoiceMarkRefundPost200ResponseData(unittest.TestCase):
    """MerchantInvoiceMarkRefundPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantInvoiceMarkRefundPost200ResponseData:
        """Test MerchantInvoiceMarkRefundPost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantInvoiceMarkRefundPost200ResponseData`
        """
        model = MerchantInvoiceMarkRefundPost200ResponseData()
        if include_optional:
            return MerchantInvoiceMarkRefundPost200ResponseData(
                refund = openapi_client.models.unibee/api/bean/refund_simplify.unibee.api.bean.RefundSimplify(
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    external_refund_id = '', 
                    gateway_id = 56, 
                    gateway_refund_id = '', 
                    merchant_id = 56, 
                    metadata = {
                        'key' : ''
                        }, 
                    payment_id = '', 
                    refund_amount = 56, 
                    refund_comment = '', 
                    refund_id = '', 
                    refund_time = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    user_id = 56, )
            )
        else:
            return MerchantInvoiceMarkRefundPost200ResponseData(
        )
        """

    def testMerchantInvoiceMarkRefundPost200ResponseData(self):
        """Test MerchantInvoiceMarkRefundPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
