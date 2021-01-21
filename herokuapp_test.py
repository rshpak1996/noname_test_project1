from pages.base_page import BasePage
from pages.page_basic_auth import Basic_Auth
from pages.page_add_remove_elements import Add_Remove_Elements
import pytest

# pytest -s -v herokuapp_test.py

# pytest -s -v herokuapp_test.py::test_add_remove_elements
def test_add_remove_elements(browser):
    page = Add_Remove_Elements(browser)
    page.open()
    page.go_to()
    page.press_the_add_element_button()
    page.should_be_delete_button()
    page.press_the_delete_button()
    page.should_disappear_delete_button()

# # # Can't switch to alert
# # pytest -s -v herokuapp_test.py::test_basic_auth
# def test_basic_auth(browser):
#     page = Basic_Auth(browser)
#     page.open()
#     page.go_to()
#     page.sign_in()
#     page.should_see_congratulations_text()

