from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.NAME, 'text')
    SUGGEST = (By.CLASS_NAME, 'mini-suggest_open')
    IMAGE_PAGE_LINK = (By.LINK_TEXT, 'Картинки')


class SearchPageLocators:
    SEARCHING_RESULT = (By.XPATH, "//a[@class='Link Link_theme_outer Path-Item link path__item link organic__greenurl']")


class ImagePageLocators:
    IMAGE_CATEGORIES = (By.CLASS_NAME, 'PopularRequestList-Item')
    IMAGE = (By.XPATH, "//img[@class='serp-item__thumb justifier__thumb']")
    IMAGE_PREVIEW = (By.CLASS_NAME, 'MMImage-Preview')
    BUTTON_NEXT_IMAGE = (By.CLASS_NAME, "CircleButton_type_next")
    BUTTON_PREVIOUS_IMAGE = (By.CLASS_NAME, "CircleButton_type_prev")
