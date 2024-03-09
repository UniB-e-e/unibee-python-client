# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_search_key_search_get200_response_data import MerchantSearchKeySearchGet200ResponseData

class TestMerchantSearchKeySearchGet200ResponseData(unittest.TestCase):
    """MerchantSearchKeySearchGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSearchKeySearchGet200ResponseData:
        """Test MerchantSearchKeySearchGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSearchKeySearchGet200ResponseData`
        """
        model = MerchantSearchKeySearchGet200ResponseData()
        if include_optional:
            return MerchantSearchKeySearchGet200ResponseData(
                match_invoice = [
                    openapi_client.models.unibee/internal/model/entity/oversea_pay/invoice.unibee.internal.model.entity.oversea_pay.Invoice(
                        biz_type = 56, 
                        create_time = 56, 
                        currency = '', 
                        data = '', 
                        gateway_id = 56, 
                        gateway_invoice_id = '', 
                        gateway_invoice_pdf = '', 
                        gateway_payment_id = '', 
                        gateway_status = '', 
                        gmt_create = '', 
                        gmt_modify = '', 
                        id = 56, 
                        invoice_id = '', 
                        invoice_name = '', 
                        is_deleted = 56, 
                        lines = '', 
                        link = '', 
                        merchant_id = 56, 
                        payment_id = '', 
                        payment_link = '', 
                        period_end = 56, 
                        period_end_time = '', 
                        period_start = 56, 
                        period_start_time = '', 
                        refund_id = '', 
                        send_email = '', 
                        send_note = '', 
                        send_pdf = '', 
                        send_status = 56, 
                        send_terms = '', 
                        status = 56, 
                        subscription_amount = 56, 
                        subscription_amount_excluding_tax = 56, 
                        subscription_id = '', 
                        tax_amount = 56, 
                        tax_scale = 56, 
                        total_amount = 56, 
                        total_amount_excluding_tax = 56, 
                        unique_id = '', 
                        user_id = 56, )
                    ],
                match_user_accounts = [
                    openapi_client.models.unibee/internal/model/entity/oversea_pay/user_account.unibee.internal.model.entity.oversea_pay.UserAccount(
                        address = '', 
                        avatar_url = '', 
                        billing_type = 56, 
                        birthday = '', 
                        company_name = '', 
                        country_code = '', 
                        country_name = '', 
                        create_time = 56, 
                        custom = '', 
                        email = '', 
                        external_user_id = '', 
                        facebook = '', 
                        first_name = '', 
                        gateway_id = '', 
                        gender = '', 
                        gmt_create = '', 
                        gmt_modify = '', 
                        id = 56, 
                        is_deleted = 56, 
                        is_risk = 56, 
                        is_special = 56, 
                        last_login_at = 56, 
                        last_name = '', 
                        linked_in = '', 
                        merchant_id = 56, 
                        mobile = '', 
                        other_social_info = '', 
                        password = '', 
                        payment_method = '', 
                        phone = '', 
                        profession = '', 
                        re_mark = '', 
                        recurring_amount = 56, 
                        school = '', 
                        status = 56, 
                        subscription_id = '', 
                        subscription_name = '', 
                        subscription_status = 56, 
                        telegram = '', 
                        tik_tok = '', 
                        time_zone = '', 
                        user_name = '', 
                        v_at_number = '', 
                        version = 56, 
                        we_chat = '', 
                        whats_app = '', )
                    ],
                precision_match_object = openapi_client.models.unibee/api/merchant/search/precision_match_object.unibee.api.merchant.search.PrecisionMatchObject(
                    data = openapi_client.models.data.data(), 
                    id = '', 
                    type = '', )
            )
        else:
            return MerchantSearchKeySearchGet200ResponseData(
        )
        """

    def testMerchantSearchKeySearchGet200ResponseData(self):
        """Test MerchantSearchKeySearchGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()