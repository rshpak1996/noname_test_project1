from .base_page import BasePage
from .locators import BrokenImagesLocators
from selenium.webdriver.common.by import By

class BrokenImages(BasePage):
    def go_to(self):
        self.browser.find_element(*BrokenImagesLocators.BROKEN_IMAGES_LINK).click()

    def is_image_broken(self):
        image1_src = self.browser.find_element(*BrokenImagesLocators.IMAGE1).get_attribute('src')
        image2_src = self.browser.find_element(*BrokenImagesLocators.IMAGE2).get_attribute('src')
        image3_src = self.browser.find_element(*BrokenImagesLocators.IMAGE3).get_attribute('src')
        images_src = [image1_src, image2_src, image3_src]
        n = 0
        for image_src in images_src:
            n += 1

            # # v1
            try:
                assert 'img/' in image_src
            except:
                print(f"Image{n} is broken")


            # v2
            # if 'img/' not in image_src:
            #     print(f"Image{n} is broken")
