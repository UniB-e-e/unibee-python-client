# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_bean_subscription_detail import UnibeeApiBeanSubscriptionDetail

class TestUnibeeApiBeanSubscriptionDetail(unittest.TestCase):
    """UnibeeApiBeanSubscriptionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiBeanSubscriptionDetail:
        """Test UnibeeApiBeanSubscriptionDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiBeanSubscriptionDetail`
        """
        model = UnibeeApiBeanSubscriptionDetail()
        if include_optional:
            return UnibeeApiBeanSubscriptionDetail(
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
                gateway = openapi_client.models.unibee/api/bean/gateway_simplify.unibee.api.bean.GatewaySimplify(
                    gateway_id = 56, 
                    gateway_logo = '', 
                    gateway_name = '', 
                    gateway_type = 56, ),
                plan = openapi_client.models.unibee/api/bean/plan_simplify.unibee.api.bean.PlanSimplify(
                    amount = 56, 
                    binding_addon_ids = '', 
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
                subscription = openapi_client.models.unibee/api/bean/subscription_simplify.unibee.api.bean.SubscriptionSimplify(
                    addon_data = '', 
                    amount = 56, 
                    billing_cycle_anchor = 56, 
                    cancel_at_period_end = 56, 
                    cancel_reason = '', 
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    current_period_end = 56, 
                    current_period_start = 56, 
                    dunning_time = 56, 
                    first_paid_time = 56, 
                    gas_payer = '', 
                    gateway_id = 56, 
                    gateway_item_data = '', 
                    gateway_status = '', 
                    id = 56, 
                    last_update_time = 56, 
                    latest_invoice_id = '', 
                    link = '', 
                    merchant_id = 56, 
                    metadata = {
                        'key' : ''
                        }, 
                    pending_update_id = '', 
                    plan_id = 56, 
                    quantity = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    task_time = '', 
                    tax_scale = 56, 
                    test_clock = 56, 
                    trial_end = 56, 
                    type = 56, 
                    user_id = 56, 
                    vat_number = '', ),
                unfinished_subscription_pending_update = openapi_client.models.unibee/api/bean/subscription_pending_update_detail.unibee.api.bean.SubscriptionPendingUpdateDetail(
                    addon_data = '', 
                    addons = [
                        openapi_client.models.unibee/api/bean/plan_addon_detail.unibee.api.bean.PlanAddonDetail(
                            addon_plan = openapi_client.models.unibee/api/bean/plan_simplify.unibee.api.bean.PlanSimplify(
                                amount = 56, 
                                binding_addon_ids = '', 
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
                    amount = 56, 
                    currency = '', 
                    effect_immediate = 56, 
                    effect_time = 56, 
                    gateway_id = 56, 
                    gmt_create = '', 
                    gmt_modify = '', 
                    link = '', 
                    merchant_id = 56, 
                    merchant_member = openapi_client.models.unibee/api/bean/merchant_member_simplify.unibee.api.bean.MerchantMemberSimplify(
                        create_time = 56, 
                        email = '', 
                        first_name = '', 
                        id = 56, 
                        last_name = '', 
                        merchant_id = 56, 
                        mobile = '', ), 
                    metadata = {
                        'key' : ''
                        }, 
                    note = '', 
                    paid = 56, 
                    plan = openapi_client.models.unibee/api/bean/plan_simplify.unibee.api.bean.PlanSimplify(
                        amount = 56, 
                        binding_addon_ids = '', 
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
                        plan_name = '', 
                        product_description = '', 
                        product_name = '', 
                        publish_status = 56, 
                        status = 56, 
                        tax_scale = 56, 
                        type = 56, ), 
                    plan_id = 56, 
                    proration_amount = 56, 
                    quantity = 56, 
                    status = 56, 
                    subscription_id = '', 
                    update_addon_data = '', 
                    update_addons = [
                        openapi_client.models.unibee/api/bean/plan_addon_detail.unibee.api.bean.PlanAddonDetail(
                            quantity = 56, )
                        ], 
                    update_amount = 56, 
                    update_currency = '', 
                    update_plan = , 
                    update_plan_id = 56, 
                    update_quantity = 56, 
                    update_subscription_id = '', 
                    user_id = 56, ),
                user = openapi_client.models.unibee/api/bean/user_account_simplify.unibee.api.bean.UserAccountSimplify(
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
                    id = 56, 
                    is_risk = 56, 
                    is_special = 56, 
                    last_login_at = 56, 
                    last_name = '', 
                    linked_in = '', 
                    merchant_id = 56, 
                    mobile = '', 
                    other_social_info = '', 
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
            )
        else:
            return UnibeeApiBeanSubscriptionDetail(
        )
        """

    def testUnibeeApiBeanSubscriptionDetail(self):
        """Test UnibeeApiBeanSubscriptionDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
