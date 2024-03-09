# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_system_invoice_bulk_channel_sync_req import UnibeeApiSystemInvoiceBulkChannelSyncReq

class TestUnibeeApiSystemInvoiceBulkChannelSyncReq(unittest.TestCase):
    """UnibeeApiSystemInvoiceBulkChannelSyncReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiSystemInvoiceBulkChannelSyncReq:
        """Test UnibeeApiSystemInvoiceBulkChannelSyncReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiSystemInvoiceBulkChannelSyncReq`
        """
        model = UnibeeApiSystemInvoiceBulkChannelSyncReq()
        if include_optional:
            return UnibeeApiSystemInvoiceBulkChannelSyncReq(
                merchant_id = ''
            )
        else:
            return UnibeeApiSystemInvoiceBulkChannelSyncReq(
                merchant_id = '',
        )
        """

    def testUnibeeApiSystemInvoiceBulkChannelSyncReq(self):
        """Test UnibeeApiSystemInvoiceBulkChannelSyncReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()