import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("valid_user")
        login_page.enter_password("valid_password")
        login_page.click_login()

        # Add an assertion to verify successful login
        assert "Dashboard" in self.driver.title, "Login failed or Dashboard title not found!"

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_password")
        login_page.click_login()

        # Add an assertion to verify error message or failed login
        error_message = self.driver.find_element_by_id("errorMessage").text
        assert "Invalid username or password" in error_message, "Error message not displayed or incorrect!"
