import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup():
    options = Options()
    options.add_experimental_option("w3c", False)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_devtools_protocol(setup):
    driver = setup
    devtools = driver.create_websocket_connection()

    # Example of sending a command to the DevTools protocol
    response = devtools.send_command("Page.enable", {})
    assert response['result'] is True

    # Adding an event listener
    def console_log_handler(params):
        print(f"Console log: {params}")

    devtools.add_listener("Runtime.consoleAPICalled", console_log_handler)

    # Interact with the page
    driver.get("https://www.example.com")
    driver.execute_script("console.log('Hello from DevTools!');")
