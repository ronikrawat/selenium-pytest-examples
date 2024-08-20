import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.example.com")
    yield driver
    driver.quit()


def test_combined_features(setup):
    driver = setup

    # Navigate and interact with the page
    driver.find_element(By.LINK_TEXT, "More information...").click()

    # Wait for a specific element to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    # Perform an action chain
    element = driver.find_element(By.TAG_NAME, "h1")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    # Capture a screenshot
    driver.save_screenshot("screenshot.png")

    # Retrieve and print logs
    logs = driver.get_log("browser")
    for log in logs:
        print(f"Log: {log['message']}, Level: {log['level']}")
