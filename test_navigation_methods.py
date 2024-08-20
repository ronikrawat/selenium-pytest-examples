import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_navigation_methods(setup):
    driver = setup

    # Navigate to first URL
    driver.get("https://www.example1.com")

    # Navigate to second URL
    driver.get("https://www.example2.com")

    # Navigate back to the first URL
    driver.back()
    assert "example1" in driver.current_url

    # Navigate forward to the second URL
    driver.forward()
    assert "example2" in driver.current_url

    # Refresh the current page
    driver.refresh()
