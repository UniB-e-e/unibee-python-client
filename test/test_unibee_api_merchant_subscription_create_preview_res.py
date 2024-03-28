# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_subscription_create_preview_res import UnibeeApiMerchantSubscriptionCreatePreviewRes

class TestUnibeeApiMerchantSubscriptionCreatePreviewRes(unittest.TestCase):
    """UnibeeApiMerchantSubscriptionCreatePreviewRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantSubscriptionCreatePreviewRes:
        """Test UnibeeApiMerchantSubscriptionCreatePreviewRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantSubscriptionCreatePreviewRes`
        """
        model = UnibeeApiMerchantSubscriptionCreatePreviewRes()
        if include_optional:
            return UnibeeApiMerchantSubscriptionCreatePreviewRes(
                addon_params = [
                    openapi_client.models.unibee/api/bean/plan_addon_param.unibee.api.bean.PlanAddonParam(
                        addon_plan_id = 56, 
                        quantity = 56, )
                    ],
                addons = [
                    openapi_client.models.unibee/api/bean/plan_addon_detail.unibee.api.bean.PlanAddonDetail(
                        addon_plan = openapi_client.models.unibee/api/bean/plan_simplify.unibee.api.bean.PlanSimplify(
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
                            tax_scale = 56, 
                            type = 56, ), 
                        quantity = 56, )
                    ],
                currency = '',
                email = '',
                gateway = openapi_client.models.unibee/api/bean/gateway_simplify.unibee.api.bean.GatewaySimplify(
                    country_config = {
                        'key' : True
                        }, 
                    gateway_id = 56, 
                    gateway_logo = '', 
                    gateway_name = '', 
                    gateway_type = 56, ),
                invoice = openapi_client.models.unibee/api/bean/invoice_simplify.unibee.api.bean.InvoiceSimplify(
                    biz_type = 56, 
                    crypto_amount = 56, 
                    crypto_currency = '', 
                    currency = '', 
                    day_util_due = 56, 
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
                            proration = True, 
                            quantity = 56, 
                            tax = 56, 
                            tax_scale = 56, 
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
                    tax_scale = 56, 
                    total_amount = 56, 
                    total_amount_excluding_tax = 56, ),
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
                    tax_scale = 56, 
                    type = 56, ),
                quantity = 56,
                tax_scale = 56,
                total_amount = 56,
                user_id = 56,
                vat_country_code = '',
                vat_country_name = '',
                vat_number = '',
                vat_number_validate = openapi_client.models.unibee/api/bean/valid_result.unibee.api.bean.ValidResult(
                    company_address = '', 
                    company_name = '', 
                    country_code = '', 
                    valid = True, 
                    validate_message = '', 
                    vat_number = '', )
            )
        else:
            return UnibeeApiMerchantSubscriptionCreatePreviewRes(
        )
        """

    def testUnibeeApiMerchantSubscriptionCreatePreviewRes(self):
        """Test UnibeeApiMerchantSubscriptionCreatePreviewRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
