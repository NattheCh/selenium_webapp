import pytest

from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("Test case 2")
    @allure.description("Searching hotels")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("dubai")
        search_hotel_page.set_date_range("31/12/2020", "01/01/2021")
        search_hotel_page.set_travelers("1", "1")
        search_hotel_page.perform_search()
        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        price_values = results_page.get_hotel_prices()

        correct_hotel_name = ["Jumeirah Beach Hotel", "Oasis Beach Tower", "Rose Rayhaan Rotana", "Hyatt Regency Perth"]
        for hotel in range(4):
            assert hotel_names[hotel] == correct_hotel_name[hotel]

        assert price_values[0] == "$25"
        assert price_values[1] == "$50"
        assert price_values[2] == "$80"
        assert price_values[3] == "$150"
