import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_alert_handling(setup):
    driver = setup
    driver.execute_script("alert('This is an alert');")

    # Switch to alert and accept it
    alert = Alert(driver)
    assert alert.text == "This is an alert"
    alert.accept()

    # Dismiss an alert
    # alert.dismiss()

    # If dealing with a prompt, send text to it
    # alert.send_keys("Sample text")
    # alert.accept()
