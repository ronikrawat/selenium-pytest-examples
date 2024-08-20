import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_webdriver_methods(setup):
    driver = setup
    driver.get("https://www.example.com")

    # Get title of the page
    assert driver.title == "Example Domain"

    # Get current URL
    assert driver.current_url == "https://www.example.com/"

    # Refresh the page
    driver.refresh()

    # Get page source
    page_source = driver.page_source
    assert "<h1>Example Domain</h1>" in page_source

    # Take a screenshot
    driver.get_screenshot_as_file("screenshot.png")
