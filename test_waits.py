import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_waits(setup):
    driver = setup

    # Implicit wait (applies to all find_element calls)
    driver.implicitly_wait(10)

    # Explicit wait (waits for a specific condition)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert element.text == "Example Domain"

    # Wait until an element is no longer visible
    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
