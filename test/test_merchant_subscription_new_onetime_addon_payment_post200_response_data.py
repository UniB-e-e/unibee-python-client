# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_subscription_new_onetime_addon_payment_post200_response_data import MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData

class TestMerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData(unittest.TestCase):
    """MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData:
        """Test MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData`
        """
        model = MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData()
        if include_optional:
            return MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData(
                invoice = openapi_client.models.unibee/api/bean/invoice_simplify.unibee.api.bean.InvoiceSimplify(
                    biz_type = 56, 
                    crypto_amount = 56, 
                    crypto_currency = '', 
                    currency = '', 
                    day_util_due = 56, 
                    discount_amount = 56, 
                    discount_code = '', 
                    finish_time = 56, 
                    id = 56, 
                    invoice_id = '', 
                    invoice_name = '', 
                    lines = [
                        openapi_client.models.unibee/api/bean/invoice_item_simplify.unibee.api.bean.InvoiceItemSimplify(
                            amount = 56, 
                            amount_excluding_tax = 56, 
                            currency = '', 
                            description = '', 
                            period_end = 56, 
                            period_start = 56, 
                            plan = openapi_client.models.unibee/api/bean/plan_simplify.unibee.api.bean.PlanSimplify(
                                amount = 56, 
                                binding_addon_ids = '', 
                                binding_onetime_addon_ids = '', 
                                create_time = 56, 
                                currency = '', 
                                description = '', 
                                extra_metric_data = '', 
                                gas_payer = '', 
                                home_url = '', 
                                id = 56, 
                                image_url = '', 
                                interval_count = 56, 
                                interval_unit = '', 
                                merchant_id = 56, 
                                metadata = {
                                    'key' : ''
                                    }, 
                                plan_name = '', 
                                product_description = '', 
                                product_name = '', 
                                publish_status = 56, 
                                status = 56, 
                                tax_percentage = 56, 
                                type = 56, ), 
                            proration = True, 
                            quantity = 56, 
                            tax = 56, 
                            tax_percentage = 56, 
                            unit_amount_excluding_tax = 56, )
                        ], 
                    link = '', 
                    payment_id = '', 
                    payment_link = '', 
                    period_end = 56, 
                    period_start = 56, 
                    proration_date = 56, 
                    proration_scale = 56, 
                    refund_id = '', 
                    send_status = 56, 
                    status = 56, 
                    subscription_amount = 56, 
                    subscription_amount_excluding_tax = 56, 
                    tax_amount = 56, 
                    tax_percentage = 56, 
                    total_amount = 56, 
                    total_amount_excluding_tax = 56, ),
                link = '',
                paid = True,
                subscription_onetime_addon = openapi_client.models.unibee/api/bean/subscription_onetime_addon_simplify.unibee.api.bean.SubscriptionOnetimeAddonSimplify(
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
                    subscription_id = '', )
            )
        else:
            return MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData(
        )
        """

    def testMerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData(self):
        """Test MerchantSubscriptionNewOnetimeAddonPaymentPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
