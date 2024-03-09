# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_time_line_detail_vo import UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo

class TestUnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo(unittest.TestCase):
    """UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo:
        """Test UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo`
        """
        model = UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo()
        if include_optional:
            return UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo(
                addons = [
                    openapi_client.models.unibee/internal/logic/gateway/ro/plan_addon_vo.unibee.internal.logic.gateway.ro.PlanAddonVo(
                        addon_plan = openapi_client.models.unibee/internal/logic/gateway/ro/plan_simplify.unibee.internal.logic.gateway.ro.PlanSimplify(
                            amount = 56, 
                            binding_addon_ids = '', 
                            create_time = 56, 
                            currency = '', 
                            description = '', 
                            extra_metric_data = '', 
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
                        quantity = 56, )
                    ],
                create_time = 56,
                currency = '',
                gateway_id = 56,
                invoice_id = '',
                merchant_id = 56,
                period_end = 56,
                period_end_time = '',
                period_start = 56,
                period_start_time = '',
                plan = openapi_client.models.unibee/internal/logic/gateway/ro/plan_simplify.unibee.internal.logic.gateway.ro.PlanSimplify(
                    amount = 56, 
                    binding_addon_ids = '', 
                    create_time = 56, 
                    currency = '', 
                    description = '', 
                    extra_metric_data = '', 
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
                quantity = 56,
                subscription_id = '',
                unique_id = '',
                user_id = 56
            )
        else:
            return UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo(
        )
        """

    def testUnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo(self):
        """Test UnibeeInternalLogicGatewayRoSubscriptionTimeLineDetailVo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()