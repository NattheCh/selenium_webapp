import logging


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travelers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} and check out {checkout} dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(check_out)

    def set_travelers(self, adults, child):
        self.logger.info("Setting travelers: adults - {adults} and child - {kids}".format(adults=adults, kids=child))
        self.driver.find_element_by_id(self.travelers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adults)
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element_by_xpath(self.search_button_xpath).click()