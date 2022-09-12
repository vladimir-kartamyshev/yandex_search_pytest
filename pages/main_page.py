from selenium.webdriver import Keys

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_search_field(self) -> bool:
        self.is_element_present(*MainPageLocators.SEARCH_FIELD)
        return True

    def enter_request_in_the_search_field(self, request):
        self.is_element_present(*MainPageLocators.SEARCH_FIELD)
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(request)

    def should_be_suggest_after_entering_request(self)-> bool:
        return self.is_element_present(*MainPageLocators.SUGGEST)

    def press_enter_in_the_search_field(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)

    def should_be_link_to_image_page(self) -> bool:
        return self.is_element_present(*MainPageLocators.IMAGE_PAGE_LINK)

    def click_link_to_image_page(self):
        self.driver.find_element(*MainPageLocators.IMAGE_PAGE_LINK).click()