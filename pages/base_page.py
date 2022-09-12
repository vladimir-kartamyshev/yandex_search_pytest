from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .locators import MainPageLocators


class BasePage():
    def __init__(self, driver: WebDriver, url, timeout=4):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((how, what)))
            # self.browser.find_element(how, what)
        except (TimeoutException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_search_field(self) -> bool:
        self.is_element_present(*MainPageLocators.SEARCH_FIELD)
        return True

    def enter_request_in_the_search_field(self, request):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(request)

    def should_be_suggest_after_entering_request(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'mini-suggest_open')))
        return True

    def should_be_current_url(self, expected_url) -> bool:
        current_url = self.driver.current_url
        return expected_url in current_url

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


