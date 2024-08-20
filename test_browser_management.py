import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_browser_management(setup):
    driver = setup

    # Get available log types
    log_types = driver.log_types
    assert "browser" in log_types

    # Get browser logs
    logs = driver.get_log("browser")
    for log in logs:
        print(f"Log: {log['message']}, Level: {log['level']}")

    # Get page source
    page_source = driver.page_source
    assert "<title>Example Domain</title>" in page_source
