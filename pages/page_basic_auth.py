from .base_page import BasePage
from .locators import BasicAuthLocators


class Basic_Auth(BasePage):
    def go_to(self):
        self.browser.find_element(*BasicAuthLocators.BASIC_AUTH_LINK).click()

    def sign_in(self):
        pass