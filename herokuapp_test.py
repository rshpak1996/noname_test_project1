import pytest
from pages.base_page import BasePage
from pages.page_add_remove_elements import Add_Remove_Elements
from pages.page_basic_auth import Basic_Auth
from pages.page_broken_images import BrokenImages
from pages.page_checkboxes import Checkboxes
from pages.page_context_menu import ContextMenu

from pages.locators import ContextMenuLocators


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

# pytest -s -v herokuapp_test.py::test_broken_images
def test_broken_images(browser):
    page = BrokenImages(browser)
    page.open()
    page.go_to()
    page.is_image_broken()

# pytest -s -v herokuapp_test.py::test_checkboxes
def test_checkboxes(browser):
    page = Checkboxes(browser)
    page.open()
    page.go_to()
    page.find_and_click_empy_checkbox()
    page.find_and_click_checked_checkbox()

# pytest -s -v herokuapp_test.py::test_context_menu
def test_context_menu(browser):
    page = ContextMenu(browser)
    page.open()
    page.go_to()
    page.should_be_context_menu_field()
    page.open_context_menu()