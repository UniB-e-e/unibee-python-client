# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.invoice import Invoice


class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self) -> None:
        self.api = Invoice()

    def tearDown(self) -> None:
        pass

    def test_invoice_cancel_post(self) -> None:
        """Test case for invoice_cancel_post

        Admin Cancel Invoice Of Processing Status
        """
        pass

    def test_invoice_delete_post(self) -> None:
        """Test case for invoice_delete_post

        Admin Delete Invoice Of Pending Status
        """
        pass

    def test_invoice_detail_get(self) -> None:
        """Test case for invoice_detail_get

        Invoice Detail
        """
        pass

    def test_invoice_detail_post(self) -> None:
        """Test case for invoice_detail_post

        Invoice Detail
        """
        pass

    def test_invoice_edit_post(self) -> None:
        """Test case for invoice_edit_post

        Admin Edit Invoice
        """
        pass

    def test_invoice_finish_post(self) -> None:
        """Test case for invoice_finish_post

        Admin Finish Invoice，Generate Pay Link
        """
        pass

    def test_invoice_list_get(self) -> None:
        """Test case for invoice_list_get

        Invoice List
        """
        pass

    def test_invoice_list_post(self) -> None:
        """Test case for invoice_list_post

        Invoice List
        """
        pass

    def test_invoice_new_post(self) -> None:
        """Test case for invoice_new_post

        Admin Create New Invoice
        """
        pass

    def test_invoice_pdf_generate_post(self) -> None:
        """Test case for invoice_pdf_generate_post

        Admin Generate Merchant Invoice pdf
        """
        pass

    def test_invoice_refund_post(self) -> None:
        """Test case for invoice_refund_post

        Admin Create Refund From Invoice
        """
        pass

    def test_invoice_send_email_post(self) -> None:
        """Test case for invoice_send_email_post

        Admin Send Merchant Invoice Email to User
        """
        pass


if __name__ == '__main__':
    unittest.main()