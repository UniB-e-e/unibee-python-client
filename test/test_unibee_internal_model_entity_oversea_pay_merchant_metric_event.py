# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_model_entity_oversea_pay_merchant_metric_event import UnibeeInternalModelEntityOverseaPayMerchantMetricEvent

class TestUnibeeInternalModelEntityOverseaPayMerchantMetricEvent(unittest.TestCase):
    """UnibeeInternalModelEntityOverseaPayMerchantMetricEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalModelEntityOverseaPayMerchantMetricEvent:
        """Test UnibeeInternalModelEntityOverseaPayMerchantMetricEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalModelEntityOverseaPayMerchantMetricEvent`
        """
        model = UnibeeInternalModelEntityOverseaPayMerchantMetricEvent()
        if include_optional:
            return UnibeeInternalModelEntityOverseaPayMerchantMetricEvent(
                aggregation_property_data = '',
                aggregation_property_int = 56,
                aggregation_property_string = '',
                aggregation_property_unique_id = '',
                create_time = 56,
                external_event_id = '',
                gmt_create = '',
                gmt_modify = '',
                id = 56,
                is_deleted = 56,
                merchant_id = 56,
                metric_id = 56,
                metric_limit = 56,
                subscription_ids = '',
                subscription_period_end = 56,
                subscription_period_start = 56,
                used = 56,
                user_id = 56
            )
        else:
            return UnibeeInternalModelEntityOverseaPayMerchantMetricEvent(
        )
        """

    def testUnibeeInternalModelEntityOverseaPayMerchantMetricEvent(self):
        """Test UnibeeInternalModelEntityOverseaPayMerchantMetricEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()