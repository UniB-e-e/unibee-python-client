# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_payment_method_get_get200_response_data import MerchantPaymentMethodGetGet200ResponseData

class TestMerchantPaymentMethodGetGet200ResponseData(unittest.TestCase):
    """MerchantPaymentMethodGetGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantPaymentMethodGetGet200ResponseData:
        """Test MerchantPaymentMethodGetGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantPaymentMethodGetGet200ResponseData`
        """
        model = MerchantPaymentMethodGetGet200ResponseData()
        if include_optional:
            return MerchantPaymentMethodGetGet200ResponseData(
                method = openapi_client.models.unibee/api/bean/payment_method.unibee.api.bean.PaymentMethod(
                    data = openapi_client.models.data.data(), 
                    id = '', 
                    type = '', )
            )
        else:
            return MerchantPaymentMethodGetGet200ResponseData(
        )
        """

    def testMerchantPaymentMethodGetGet200ResponseData(self):
        """Test MerchantPaymentMethodGetGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()