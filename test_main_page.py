import pytest

from .pages.main_page import MainPage
from .pages.search_page import SearchPage

TEST_DATA = [
    ("https://yandex.ru/", "Тензор", 1, "https://tensor.ru/")
]


@pytest.mark.parametrize("link, query, index_search_result, expected_link", TEST_DATA)
def test_search_position(driver, link, query, index_search_result, expected_link):
    main_page = MainPage(driver, link)
    main_page.open()
    assert main_page.should_be_search_field()
    main_page.enter_request_in_the_search_field(query)
    assert main_page.should_be_suggest_after_entering_request()
    main_page.press_enter_in_the_search_field()
    search_page = SearchPage(driver, link)
    assert search_page.should_be_searching_result()
    assert search_page.get_link_to_search_result(index_search_result) == expected_link
