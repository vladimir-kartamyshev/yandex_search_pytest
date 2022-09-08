import pytest

from .pages.image_page import ImagePage
from .pages.main_page import MainPage

TEST_DATA = [
    ("https://yandex.ru/", "https://yandex.ru/images/", 1, 1)
]


@pytest.mark.parametrize("url, expected_url, category_number, image_number", TEST_DATA)
def test_change_image(driver, url, expected_url, category_number, image_number):
    # url = "https://yandex.ru/"
    # expected_url = "https://yandex.ru/images/"
    # category_number = 1
    # image_number = 1
    main_page = MainPage(driver, url)
    main_page.open()
    assert main_page.should_be_link_to_image_page()
    main_page.click_link_to_image_page()
    image_page = ImagePage(driver, url)
    image_page.switch_to_new_window()
    assert image_page.should_be_current_url(expected_url)
    image_page.click_image_category_number(category_number)
    assert image_page.should_be_valid_category_name_in_search_field(category_number)
    image_page.click_image_number(image_number)
    assert image_page.should_be_image_opened()
    src_image = image_page.get_src_image()
    image_page.click_next_image()
    assert not src_image == image_page.get_src_image()
    image_page.click_previous_image()
    assert src_image == image_page.get_src_image()
