from .base_page import BasePage
from .locators import CheckboxesLocators

class Checkboxes(BasePage):
    def go_to(self):
        self.browser.find_element(*CheckboxesLocators.CHECKBOXES_LINK).click()
    
    def find_and_click_empy_checkbox(self):
        self.browser.find_element(*CheckboxesLocators.EMPTY_CHECKBOX).click()

    def find_and_click_checked_checkbox(self):
        self.browser.find_element(*CheckboxesLocators.CHECKED_CHECKBOX).click()
