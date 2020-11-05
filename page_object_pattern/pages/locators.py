class SearchHotelLocators:
    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//div[@id='select2-drop']//input"
    location_match_xpath = "//span[text()='Dubai']"
    check_in_input_name = "checkin"
    check_out_input_name = "checkout"
    travelers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    child_input_id = "childInput"
    search_button_xpath = "//button[text()=' Search']"


class SearchResultsLocators:
    hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
    hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"
