import pytest
from pages.booking_page import BookingPage

@pytest.mark.usefixtures("setup")
class TestBooking:
    def test_valid_booking(self):
        booking_page = BookingPage(self.driver)

        # Fill in booking details
        booking_page.select_flight("Flight123")
        booking_page.enter_passenger_details({
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        })
        booking_page.select_seat("12A")
        booking_page.click_continue()

        # Verify booking confirmation
        assert booking_page.is_booking_successful(), "Booking was not successful!"

    def test_invalid_booking(self):
        booking_page = BookingPage(self.driver)

        # Leave passenger details empty to simulate an invalid booking
        booking_page.select_flight("Flight123")
        booking_page.enter_passenger_details({})  # Empty details
        booking_page.click_continue()

        # Verify error message is displayed
        error_message = booking_page.get_error_message()
        assert "Passenger details are required" in error_message, "Error message not displayed or incorrect!"
