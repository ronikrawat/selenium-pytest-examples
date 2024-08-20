import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()


def test_action_chains(setup):
    driver = setup
    element = driver.find_element(By.LINK_TEXT, "Register")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Move to the element and click it
    actions.move_to_element(element).click().perform()

    # Double-click on an element
    actions.double_click(element).perform()

    # Right-click on an element
    actions.context_click(element).perform()

    # Click and hold, then release
    actions.click_and_hold(element).release().perform()

    # Drag and drop
    source = driver.find_element(By.ID, "source-element")
    target = driver.find_element(By.ID, "target-element")
    actions.drag_and_drop(source, target).perform()
