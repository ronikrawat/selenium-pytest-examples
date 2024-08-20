import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_cookie_handling(setup):
    driver = setup

    # Get all cookies
    cookies = driver.get_cookies()
    print("All cookies:", cookies)

    # Add a new cookie
    driver.add_cookie({"name": "my_cookie", "value": "cookie_value"})

    # Get a specific cookie
    cookie = driver.get_cookie("my_cookie")
    assert cookie["value"] == "cookie_value"

    # Delete a specific cookie
    driver.delete_cookie("my_cookie")

    # Delete all cookies
    driver.delete_all_cookies()
    assert len(driver.get_cookies()) == 0
