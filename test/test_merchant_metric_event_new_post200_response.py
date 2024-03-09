# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_metric_event_new_post200_response import MerchantMetricEventNewPost200Response

class TestMerchantMetricEventNewPost200Response(unittest.TestCase):
    """MerchantMetricEventNewPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantMetricEventNewPost200Response:
        """Test MerchantMetricEventNewPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantMetricEventNewPost200Response`
        """
        model = MerchantMetricEventNewPost200Response()
        if include_optional:
            return MerchantMetricEventNewPost200Response(
                code = 56,
                data = openapi_client.models._merchant_metric_event_new_post_200_response_data._merchant_metric_event_new_post_200_response_data(
                    merchant_metric_event = openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant_metric_event.unibee.internal.model.entity.oversea_pay.MerchantMetricEvent(
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
                        user_id = 56, ), ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantMetricEventNewPost200Response(
        )
        """

    def testMerchantMetricEventNewPost200Response(self):
        """Test MerchantMetricEventNewPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()