# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_logic_gateway_ro_invoice_detail_ro import UnibeeInternalLogicGatewayRoInvoiceDetailRo

class TestUnibeeInternalLogicGatewayRoInvoiceDetailRo(unittest.TestCase):
    """UnibeeInternalLogicGatewayRoInvoiceDetailRo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalLogicGatewayRoInvoiceDetailRo:
        """Test UnibeeInternalLogicGatewayRoInvoiceDetailRo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalLogicGatewayRoInvoiceDetailRo`
        """
        model = UnibeeInternalLogicGatewayRoInvoiceDetailRo()
        if include_optional:
            return UnibeeInternalLogicGatewayRoInvoiceDetailRo(
                currency = '',
                data = '',
                discount_amount = 56,
                gateway = openapi_client.models.unibee/internal/logic/gateway/ro/gateway_simplify.unibee.internal.logic.gateway.ro.GatewaySimplify(
                    gateway_id = 56, 
                    gateway_logo = '', 
                    gateway_name = '', ),
                gateway_id = 56,
                gateway_invoice_id = '',
                gateway_invoice_pdf = '',
                gateway_payment_id = '',
                gateway_status = '',
                gateway_user_id = '',
                gmt_create = '',
                gmt_modify = '',
                id = 56,
                invoice_id = '',
                invoice_name = '',
                is_deleted = 56,
                lines = [
                    openapi_client.models.unibee/internal/logic/gateway/ro/invoice_item_detail_ro.unibee.internal.logic.gateway.ro.InvoiceItemDetailRo(
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
                merchant = openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant.unibee.internal.model.entity.oversea_pay.Merchant(
                    address = '', 
                    api_key = '', 
                    business_num = '', 
                    company_id = 56, 
                    company_logo = '', 
                    company_name = '', 
                    create_time = 56, 
                    email = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    home_url = '', 
                    host = '', 
                    id = 56, 
                    idcard = '', 
                    is_deleted = 56, 
                    location = '', 
                    name = '', 
                    phone = '', 
                    time_zone = '', 
                    type = 56, 
                    user_id = 56, ),
                merchant_id = 56,
                payment = openapi_client.models.unibee/internal/model/entity/oversea_pay/payment.unibee.internal.model.entity.oversea_pay.Payment(
                    additional_data = '', 
                    app_id = '', 
                    authorize_reason = '', 
                    authorize_status = 56, 
                    automatic = 56, 
                    balance_amount = 56, 
                    balance_end = 56, 
                    balance_start = 56, 
                    billing_reason = '', 
                    biz_type = 56, 
                    cancel_time = 56, 
                    capture_delay_hours = 56, 
                    code = '', 
                    company_id = 56, 
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    external_payment_id = '', 
                    failure_reason = '', 
                    gateway_edition = '', 
                    gateway_id = 56, 
                    gateway_payment_id = '', 
                    gateway_payment_intent_id = '', 
                    gateway_payment_method = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    hide_payment_methods = '', 
                    id = 56, 
                    invoice_data = '', 
                    invoice_id = '', 
                    link = '', 
                    merchant_id = 56, 
                    open_api_id = 56, 
                    paid_time = 56, 
                    payment_amount = 56, 
                    payment_data = '', 
                    payment_id = '', 
                    refund_amount = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    terminal_ip = '', 
                    token = '', 
                    total_amount = 56, 
                    unique_id = '', 
                    user_id = 56, 
                    verify = '', ),
                payment_id = '',
                period_end = 56,
                period_start = 56,
                refund = openapi_client.models.unibee/internal/model/entity/oversea_pay/refund.unibee.internal.model.entity.oversea_pay.Refund(
                    additional_data = '', 
                    app_id = '', 
                    biz_type = 56, 
                    company_id = 56, 
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    external_refund_id = '', 
                    gateway_id = 56, 
                    gateway_refund_id = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    id = 56, 
                    merchant_id = 56, 
                    open_api_id = 56, 
                    payment_id = '', 
                    refund_amount = 56, 
                    refund_comment = '', 
                    refund_comment_explain = '', 
                    refund_id = '', 
                    refund_time = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    unique_id = '', 
                    user_id = 56, ),
                refund_id = '',
                send_email = '',
                send_note = '',
                send_pdf = '',
                send_status = 56,
                send_terms = '',
                status = 56,
                subscription = openapi_client.models.unibee/internal/model/entity/oversea_pay/subscription.unibee.internal.model.entity.oversea_pay.Subscription(
                    addon_data = '', 
                    amount = 56, 
                    billing_cycle_anchor = 56, 
                    cancel_at_period_end = 56, 
                    cancel_reason = '', 
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    current_period_end = 56, 
                    current_period_end_time = '', 
                    current_period_start = 56, 
                    current_period_start_time = '', 
                    customer_email = '', 
                    customer_name = '', 
                    data = '', 
                    dunning_time = 56, 
                    first_paid_time = 56, 
                    gateway_default_payment_method = '', 
                    gateway_id = 56, 
                    gateway_item_data = '', 
                    gateway_latest_invoice_id = '', 
                    gateway_status = '', 
                    gateway_subscription_id = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    id = 56, 
                    is_deleted = 56, 
                    last_update_time = 56, 
                    latest_invoice_id = '', 
                    link = '', 
                    merchant_id = 56, 
                    pending_update_id = '', 
                    plan_id = 56, 
                    quantity = 56, 
                    response_data = '', 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    task_time = '', 
                    tax_scale = 56, 
                    test_clock = 56, 
                    trial_end = 56, 
                    type = 56, 
                    user_id = 56, 
                    vat_number = '', 
                    vat_verify_data = '', ),
                subscription_amount = 56,
                subscription_amount_excluding_tax = 56,
                subscription_id = '',
                tax_amount = 56,
                tax_scale = 56,
                total_amount = 56,
                total_amount_excluding_tax = 56,
                unique_id = '',
                user_account = openapi_client.models.unibee/internal/model/entity/oversea_pay/user_account.unibee.internal.model.entity.oversea_pay.UserAccount(
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
                    whats_app = '', ),
                user_id = 56
            )
        else:
            return UnibeeInternalLogicGatewayRoInvoiceDetailRo(
        )
        """

    def testUnibeeInternalLogicGatewayRoInvoiceDetailRo(self):
        """Test UnibeeInternalLogicGatewayRoInvoiceDetailRo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()