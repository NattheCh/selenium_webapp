from allure_commons.types import AttachmentType

from page_object_pattern.pages.locators import SearchResultsLocators
import logging
import allure


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Checking results")
    def get_hotel_names(self):
        hotels = self.driver.find_elements_by_xpath(SearchResultsLocators.hotel_names_xpath)
        self.logger.info("Available hotels: ")
        allure.attach(self.driver.get_screenshot_as_png(), name="Results", attachment_type=AttachmentType.PNG)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        for name in names:
            self.logger.info(name)
        return names


    def get_hotel_prices(self):
        prices = self.driver.find_elements_by_xpath(SearchResultsLocators.hotel_prices_xpath)
        hotel_prices = [price.get_attribute("textContent") for price in prices]
        self.logger.info("Prices are:")
        for price in hotel_prices:
            self.logger.info(price)
        return hotel_prices