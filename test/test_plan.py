# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.plan import Plan


class TestPlan(unittest.TestCase):
    """Plan unit test stubs"""

    def setUp(self) -> None:
        self.api = Plan()

    def tearDown(self) -> None:
        pass

    def test_plan_activate_post(self) -> None:
        """Test case for plan_activate_post

        Plan Sync To Gateway And Activate
        """
        pass

    def test_plan_addons_binding_post(self) -> None:
        """Test case for plan_addons_binding_post

        Plan Binding Addons
        """
        pass

    def test_plan_delete_post(self) -> None:
        """Test case for plan_delete_post

        Delete A Plan Before Activate
        """
        pass

    def test_plan_detail_get(self) -> None:
        """Test case for plan_detail_get

        Plan Detail
        """
        pass

    def test_plan_detail_post(self) -> None:
        """Test case for plan_detail_post

        Plan Detail
        """
        pass

    def test_plan_edit_post(self) -> None:
        """Test case for plan_edit_post

        Edit Plan
        """
        pass

    def test_plan_expire_post(self) -> None:
        """Test case for plan_expire_post

        Expire A Plan
        """
        pass

    def test_plan_list_get(self) -> None:
        """Test case for plan_list_get

        Plan List
        """
        pass

    def test_plan_list_post(self) -> None:
        """Test case for plan_list_post

        Plan List
        """
        pass

    def test_plan_new_post(self) -> None:
        """Test case for plan_new_post

        Create Plan
        """
        pass

    def test_plan_publish_post(self) -> None:
        """Test case for plan_publish_post

        Publish Plan，Will Be Visible To UserPortal
        """
        pass

    def test_plan_unpublished_post(self) -> None:
        """Test case for plan_unpublished_post

        UnPublish Plan
        """
        pass


if __name__ == '__main__':
    unittest.main()
