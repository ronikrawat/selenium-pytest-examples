import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def setup():
    service = Service(executable_path="/path/to/chromedriver")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_service_driver_management(setup):
    driver = setup
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title
