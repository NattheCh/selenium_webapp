from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://www.kurs-selenium.pl/demo/")
driver.maximize_window()
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
driver.find_element_by_name("checkin").send_keys("08/09/2020")
driver.find_element_by_name("checkout").send_keys("11/09/2020")
driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("3")
driver.find_element_by_id("childPlusBtn").click()
driver.find_element_by_xpath("//button[text()=' Search']").click()
hotels = driver.find_elements_by_xpath("//h4[contains(@class, 'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)

prices = driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("The price is: " + price)

correct_hotel_name =["Jumeirah Beach Hotel", "Oasis Beach Tower", "Rose Rayhaan Rotana", "Hyatt Regency Perth"]
for hotel in range(4):
    assert hotel_names[hotel] == correct_hotel_name[hotel]

assert price_values[0] == "£14.30"
assert price_values[1] == "£32.50"
assert price_values[2] == "£52"
assert price_values[3] == "£97.50"

driver.quit()