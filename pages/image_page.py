from .base_page import BasePage
from .locators import MainPageLocators, ImagePageLocators


class ImagePage(BasePage):
    def click_image_category_number(self, number_category):
        category_results = self.driver.find_elements(*ImagePageLocators.IMAGE_CATEGORIES)[number_category - 1]
        category_results.click()

    def should_be_valid_category_name_in_search_field(self, number_category) -> bool:
        name_category = self.driver.find_elements(*ImagePageLocators.IMAGE_CATEGORIES)[number_category - 1].get_attribute("data-grid-text")
        name_category_in_field_search = self.driver.find_element(*MainPageLocators.SEARCH_FIELD).get_attribute("value")
        return name_category == name_category_in_field_search

    def click_image_number(self, image_number):
        self.is_element_present(*ImagePageLocators.IMAGE)
        image = self.driver.find_elements(*ImagePageLocators.IMAGE)[image_number - 1]
        image.click()

    def should_be_image_opened(self) -> bool:
        return self.is_element_present(*ImagePageLocators.IMAGE_PREVIEW)

    def click_next_image(self):
        self.driver.find_element(*ImagePageLocators.BUTTON_NEXT_IMAGE).click()

    def click_previous_image(self):
        self.driver.find_element(*ImagePageLocators.BUTTON_PREVIOUS_IMAGE).click()

    def get_src_image(self) -> str:
        src_image = self.driver.find_element(*ImagePageLocators.IMAGE_PREVIEW).get_attribute("src")
        return src_image
