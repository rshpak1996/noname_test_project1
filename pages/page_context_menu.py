from .base_page import BasePage
from .locators import ContextMenuLocators
from selenium.webdriver import ActionChains
import time

class ContextMenu(BasePage):
    def go_to(self):
        self.browser.find_element(*ContextMenuLocators.CONTEXT_MENU_LINK).click()

    def should_be_context_menu_field(self):
        assert self.browser.find_element(*ContextMenuLocators.CONTEXT_MENU_FIELD), "Context menu doesn't exist"

    def open_context_menu(self):
        context_menu_field = self.browser.find_element(*ContextMenuLocators.CONTEXT_MENU_FIELD)
        action = ActionChains(self.browser)
        action.context_click(context_menu_field).perform()
        self.browser.switch_to.alert.accept()