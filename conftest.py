import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--driver_name', action='store', default="chrome",
                     help="Choose driver: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose user_language: ru or us")


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption("driver_name")
    language = request.config.getoption("language")
    if driver_name == "chrome":
        print("\nstart chrome driver for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif driver_name == "remote":
        print("\nstart chrome driver for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif driver_name == "firefox":
        print("\nstart firefox driver for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), firefox_profile=fp)
    else:
        raise pytest.UsageError("--driver_name should be chrome or firefox")
    yield driver
    print("\nquit driver..")
    driver.quit()
