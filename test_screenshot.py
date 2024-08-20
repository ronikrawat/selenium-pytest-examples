from selenium import webdriver
import base64


# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open a webpage
    driver.get("https://www.example.com")

    # Take a screenshot and save it as a file
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    # Take a screenshot and get it as a base64 encoded string
    screenshot_base64 = driver.get_screenshot_as_base64()
    print("Screenshot (base64 encoded):")
    print(screenshot_base64[:100] + "...")  # Print the first 100 characters for brevity

    # Save the base64 screenshot to a file
    with open("screenshot_base64.txt", "w") as file:
        file.write(screenshot_base64)
    print("Base64 screenshot saved to screenshot_base64.txt")

finally:
    # Clean up and close the WebDriver
    driver.quit()
