import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")  # Replace with actual URL containing Shadow DOM
    yield driver
    driver.quit()


def test_shadow_dom(setup):
    driver = setup

    # Locate the element containing the shadow root
    shadow_host = driver.find_element(By.CSS_SELECTOR, "css-selector-for-shadow-host")

    # Access the shadow root
    shadow_root = shadow_host.shadow_root

    # Locate an element inside the shadow root
    shadow_element = shadow_root.find_element(By.CSS_SELECTOR, "css-selector-inside-shadow-root")

    # Perform actions on the shadow element
    assert shadow_element.text == "Expected Text"
