# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_bean_plan_metric_limit_detail import UnibeeApiBeanPlanMetricLimitDetail

class TestUnibeeApiBeanPlanMetricLimitDetail(unittest.TestCase):
    """UnibeeApiBeanPlanMetricLimitDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiBeanPlanMetricLimitDetail:
        """Test UnibeeApiBeanPlanMetricLimitDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiBeanPlanMetricLimitDetail`
        """
        model = UnibeeApiBeanPlanMetricLimitDetail()
        if include_optional:
            return UnibeeApiBeanPlanMetricLimitDetail(
                merchant_id = 56,
                metric_id = 56,
                plan_limits = [
                    openapi_client.models.unibee/api/bean/merchant_metric_plan_limit.unibee.api.bean.MerchantMetricPlanLimit(
                        create_time = 56, 
                        gmt_modify = 56, 
                        id = 56, 
                        merchant_id = 56, 
                        merchant_metric_vo = openapi_client.models.unibee/api/bean/merchant_metric_simplify.unibee.api.bean.MerchantMetricSimplify(
                            aggregation_property = '', 
                            aggregation_type = 56, 
                            code = '', 
                            create_time = 56, 
                            gmt_modify = 56, 
                            id = 56, 
                            merchant_id = 56, 
                            metric_description = '', 
                            metric_name = '', 
                            type = 56, ), 
                        metric_id = 56, 
                        metric_limit = 56, 
                        plan_id = 56, )
                    ],
                total_limit = 56,
                user_id = 56,
                aggregation_property = '',
                aggregation_type = 56,
                code = '',
                metric_name = '',
                type = 56
            )
        else:
            return UnibeeApiBeanPlanMetricLimitDetail(
        )
        """

    def testUnibeeApiBeanPlanMetricLimitDetail(self):
        """Test UnibeeApiBeanPlanMetricLimitDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
