from selenium.webdriver.common.by import By

class PaymentPage:
    # Locators
    CARD_NUMBER_INPUT = (By.ID, "cardNumber")
    CARD_EXPIRY_INPUT = (By.ID, "cardExpiry")
    CARD_CVV_INPUT = (By.ID, "cardCVV")
    CARDHOLDER_NAME_INPUT = (By.ID, "cardHolderName")
    PAY_BUTTON = (By.ID, "payButton")
    ERROR_MESSAGE = (By.ID, "errorMessage")
    SUCCESS_MESSAGE = (By.ID, "successMessage")

    def __init__(self, driver):
        self.driver = driver

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)

    def enter_card_expiry(self, expiry_date):
        self.driver.find_element(*self.CARD_EXPIRY_INPUT).send_keys(expiry_date)

    def enter_card_cvv(self, cvv):
        self.driver.find_element(*self.CARD_CVV_INPUT).send_keys(cvv)

    def enter_cardholder_name(self, name):
        self.driver.find_element(*self.CARDHOLDER_NAME_INPUT).send_keys(name)

    def click_pay(self):
        self.driver.find_element(*self.PAY_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def is_payment_successful(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).is_displayed()
