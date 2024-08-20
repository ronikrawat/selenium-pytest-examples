import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_options_management(setup):
    driver = setup
    driver.get("https://www.example.com")

    # Test if running in headless mode
    assert driver.execute_script("return navigator.userAgent;").find("Headless") != -1
