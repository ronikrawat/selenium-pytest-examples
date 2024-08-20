import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_webelement_methods(setup):
    driver = setup
    element = driver.find_element(By.TAG_NAME, "h1")

    # Get text
    assert element.text == "Example Domain"

    # Check if displayed
    assert element.is_displayed()

    # Get CSS value
    font_size = element.value_of_css_property("font-size")
    assert font_size == "2em"

    # Get attribute
    assert element.get_attribute("id") == "some-id"  # Example usage
