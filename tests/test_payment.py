import pytest
from pages.payment_page import PaymentPage

@pytest.mark.usefixtures("setup")
class TestPayment:
    def test_valid_payment(self):
        payment_page = PaymentPage(self.driver)

        # Fill in payment details
        payment_page.enter_card_number("4111111111111111")
        payment_page.enter_card_expiry("12/26")
        payment_page.enter_card_cvv("123")
        payment_page.enter_cardholder_name("John Doe")
        payment_page.click_pay()

        # Verify payment confirmation
        assert payment_page.is_payment_successful(), "Payment was not successful!"

    def test_invalid_payment(self):
        payment_page = PaymentPage(self.driver)

        # Fill in invalid payment details
        payment_page.enter_card_number("1234567890123456")  # Invalid card number
        payment_page.enter_card_expiry("12/20")  # Expired card
        payment_page.enter_card_cvv("000")
        payment_page.enter_cardholder_name("John Doe")
        payment_page.click_pay()

        # Verify error message for invalid payment
        error_message = payment_page.get_error_message()
        assert "Invalid card details" in error_message, "Error message not displayed or incorrect!"
