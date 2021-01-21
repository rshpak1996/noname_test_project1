from selenium.webdriver.common.by import By


class AddRemoveElementsLocators():
    ADD_REMOVE_ELEMENTS_LINK = (By.CSS_SELECTOR, '[href="/add_remove_elements/"]')
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[onclick="deleteElement()"]')

class BasicAuthLocators():
    BASIC_AUTH_LINK = (By.CSS_SELECTOR, '[href="/basic_auth"]')    