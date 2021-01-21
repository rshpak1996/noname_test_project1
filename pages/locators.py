from selenium.webdriver.common.by import By

class BasePageLocators():
    ADD_REMOVE_ELEMENTS_LINK = (By.CSS_SELECTOR, '[href="/add_remove_elements/"]')

class AddRemoveElementsLocators():
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[onclick="deleteElement()"]')
