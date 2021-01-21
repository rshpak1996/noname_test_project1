from pages.base_page import BasePage
from pages.page_add_remove_elements import Add_Remove_Elements
import pytest

# pytest -s -v herokuapp_test.py


@pytest.mark.add_remove_elements
def test_add_remove_elements(browser):
    page = Add_Remove_Elements(browser)
    page.open()
    page.go_to()
    page.press_the_add_element_button()
    page.should_be_delete_button()
    page.press_the_delete_button()
    page.should_disappear_delete_button()

