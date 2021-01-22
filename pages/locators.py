from selenium.webdriver.common.by import By


class AddRemoveElementsLocators():
    ADD_REMOVE_ELEMENTS_LINK = (By.CSS_SELECTOR, '[href="/add_remove_elements/"]')
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, '[onclick="addElement()"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '[onclick="deleteElement()"]')

class BasicAuthLocators():
    BASIC_AUTH_LINK = (By.CSS_SELECTOR, '[href="/basic_auth"]')

class BrokenImagesLocators():
    BROKEN_IMAGES_LINK = (By.CSS_SELECTOR, '[href="/broken_images"]')
    IMAGE1 = (By.CSS_SELECTOR, 'div.example > img:nth-child(2)')
    IMAGE2 = (By.CSS_SELECTOR, 'div.example > img:nth-child(3)')
    IMAGE3 = (By.CSS_SELECTOR, 'div.example > img:nth-child(4)')

class CheckboxesLocators():
    CHECKBOXES_LINK = (By.CSS_SELECTOR, '[href="/checkboxes"]')
    EMPTY_CHECKBOX = (By.CSS_SELECTOR, '#checkboxes > input:nth-child(1)')
    CHECKED_CHECKBOX = (By.CSS_SELECTOR, '#checkboxes > input:nth-child(3)')

class ContextMenuLocators():
    CONTEXT_MENU_LINK = (By.CSS_SELECTOR, '[href="/context_menu"]')
    CONTEXT_MENU_FIELD = (By.CSS_SELECTOR, '[oncontextmenu="displayMessage()"]')