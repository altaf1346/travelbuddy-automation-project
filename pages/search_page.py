from selenium.webdriver.common.by import By

class SearchPage:
    # Locators
    DEPARTURE_CITY_INPUT = (By.ID, "departureCity")
    DESTINATION_CITY_INPUT = (By.ID, "destinationCity")
    DEPARTURE_DATE_INPUT = (By.ID, "departureDate")
    RETURN_DATE_INPUT = (By.ID, "returnDate")
    SEARCH_BUTTON = (By.ID, "searchButton")
    SEARCH_RESULTS = (By.ID, "searchResults")
    ERROR_MESSAGE = (By.ID, "errorMessage")

    def __init__(self, driver):
        self.driver = driver

    def enter_departure_city(self, city):
        self.driver.find_element(*self.DEPARTURE_CITY_INPUT).send_keys(city)

    def enter_destination_city(self, city):
        self.driver.find_element(*self.DESTINATION_CITY_INPUT).send_keys(city)

    def select_departure_date(self, date):
        self.driver.find_element(*self.DEPARTURE_DATE_INPUT).send_keys(date)

    def select_return_date(self, date):
        self.driver.find_element(*self.RETURN_DATE_INPUT).send_keys(date)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def is_search_results_displayed(self):
        return self.driver.find_element(*self.SEARCH_RESULTS).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
