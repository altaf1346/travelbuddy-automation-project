from selenium.webdriver.common.by import By

class BookingPage:
    # Locators
    FLIGHT_SELECTION = (By.ID, "flightSelection")
    PASSENGER_DETAILS_FORM = (By.ID, "passengerDetailsForm")
    CONTINUE_BUTTON = (By.ID, "continueButton")
    SEAT_SELECTION = (By.ID, "seatSelection")
    ERROR_MESSAGE = (By.ID, "errorMessage")
    SUCCESS_MESSAGE = (By.ID, "successMessage")

    def __init__(self, driver):
        self.driver = driver

    def select_flight(self, flight_id):
        self.driver.find_element(By.ID, flight_id).click()

    def enter_passenger_details(self, passenger_details):
        form = self.driver.find_element(*self.PASSENGER_DETAILS_FORM)
        form.find_element(By.NAME, "firstName").send_keys(passenger_details.get("first_name", ""))
        form.find_element(By.NAME, "lastName").send_keys(passenger_details.get("last_name", ""))
        form.find_element(By.NAME, "email").send_keys(passenger_details.get("email", ""))
        form.find_element(By.NAME, "phone").send_keys(passenger_details.get("phone", ""))

    def select_seat(self, seat_number):
        self.driver.find_element(By.ID, seat_number).click()

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_booking_successful(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()
