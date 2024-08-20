import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_locating_elements(setup):
    driver = setup

    # Locate element by ID
    element = driver.find_element(By.ID, "element-id")
    assert element is not None

    # Locate element by name
    element = driver.find_element(By.NAME, "element-name")
    assert element is not None

    # Locate element by class name
    element = driver.find_element(By.CLASS_NAME, "element-class")
    assert element is not None

    # Locate element by CSS selector
    element = driver.find_element(By.CSS_SELECTOR, "div.element-class")
    assert element is not None

    # Locate element by XPath
    element = driver.find_element(By.XPATH, "//div[@class='element-class']")
    assert element is not None
