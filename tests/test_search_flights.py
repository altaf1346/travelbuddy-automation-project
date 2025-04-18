import pytest
from pages.search_page import SearchPage

@pytest.mark.usefixtures("setup")
class TestSearchFlights:
    def test_valid_flight_search(self):
        search_page = SearchPage(self.driver)
        
        # Enter flight search details
        search_page.enter_departure_city("New York")
        search_page.enter_destination_city("London")
        search_page.select_departure_date("2025-05-01")
        search_page.select_return_date("2025-05-15")
        search_page.click_search()

        # Verify search results are displayed
        assert search_page.is_search_results_displayed(), "Flight search results were not displayed!"

    def test_invalid_flight_search(self):
        search_page = SearchPage(self.driver)
        
        # Leave destination city empty to simulate invalid input
        search_page.enter_departure_city("New York")
        search_page.enter_destination_city("")  # Invalid input
        search_page.select_departure_date("2025-05-01")
        search_page.select_return_date("2025-05-15")
        search_page.click_search()

        # Verify error message is displayed
        error_message = search_page.get_error_message()
        assert "Please enter a valid destination" in error_message, "Error message not displayed or incorrect!"
