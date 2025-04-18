import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config import Config

@pytest.fixture(scope="class")
def setup(request):
    """
    Pytest fixture to set up and tear down the WebDriver.
    """
    browser = Config.BROWSER.lower()  # Get browser from config.py (default: chrome)

    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        service = ChromeService()  # Adjust if you have a specific chromedriver path
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        service = FirefoxService()  # Adjust if you have a specific geckodriver path
        driver = webdriver.Firefox(service=service, options=firefox_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(Config.BASE_URL)  # Navigate to the base URL
    request.cls.driver = driver

    yield
    driver.quit()  # Quit the browser after tests are complete
