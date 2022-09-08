from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_searching_result(self) -> bool:
        return self.is_element_present(*SearchPageLocators.SEARCHING_RESULT)

    def get_link_to_search_result(self, index) -> str:
        href = self.driver.find_elements(*SearchPageLocators.SEARCHING_RESULT)[index - 1].get_attribute("href")
        return href
