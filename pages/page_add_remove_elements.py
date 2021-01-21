from .base_page import BasePage
from .locators import BasePageLocators, AddRemoveElementsLocators
import time

class Add_Remove_Elements(BasePage):
    def go_to(self):
        link = self.browser.find_element(*BasePageLocators.ADD_REMOVE_ELEMENTS_LINK)
        link.click()

    def press_the_add_element_button(self):
        self.browser.find_element(*AddRemoveElementsLocators.ADD_ELEMENT_BUTTON).click()
        time.sleep(1)
    
    def should_be_delete_button(self):
        assert self.is_element_present(*AddRemoveElementsLocators.DELETE_BUTTON), "Delete Button doesn't exist"

    def press_the_delete_button(self):
        self.browser.find_element(*AddRemoveElementsLocators.DELETE_BUTTON).click()

    def should_disappear_delete_button(self):
        assert self.is_disappeared(*AddRemoveElementsLocators.DELETE_BUTTON), "Delete Button didn't disappear"

    