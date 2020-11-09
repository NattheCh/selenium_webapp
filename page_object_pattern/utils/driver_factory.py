from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        raise Exception("Provide valid driver name")