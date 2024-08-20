# Selenium with pytest - Python Examples

This repository contains a comprehensive collection of examples demonstrating the use of Selenium with pytest in Python. The examples cover a wide range of Selenium features, from basic WebDriver methods to advanced concepts like Shadow DOM interaction and DevTools protocol.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [Features Covered](#features-covered)
   - WebDriver Methods
   - WebElement Methods
   - Locating Elements
   - Navigation Methods
   - Alert Handling
   - Action Chains
   - Waits
   - Cookie Handling
   - Options Management
   - Service and Driver Management
   - Browser Management
   - Shadow DOM Interaction
4. [Running Tests](#running-tests)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Getting Started

To get started, clone this repository to your local machine and navigate to the project directory.

```bash
git clone https://github.com/ronikrawat/selenium-pytest-examples.git
cd selenium-pytest-examples
```

## Installation

1. **Install Python**: Ensure that you have Python 3.8 or later installed on your system.

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Requirements

- `selenium`
- `pytest`
- `webdriver-manager`

## Features Covered

### WebDriver Methods

Examples include:

- `get(url)`
- `close()`
- `quit()`
- `maximize_window()`
- `get_screenshot_as_file(filename)`

### WebElement Methods

Examples include:

- `click()`
- `send_keys(*value)`
- `get_attribute(name)`
- `is_displayed()`

### Locating Elements

Examples include:

- `find_element(By.ID, value)`
- `find_elements(By.CSS_SELECTOR, value)`

### Navigation Methods

Examples include:

- `switch_to.window(window_name)`
- `switch_to.frame(frame_reference)`

### Alert Handling

Examples include:

- `accept()`
- `dismiss()`

### Action Chains

Examples include:

- `move_to_element(to_element)`
- `drag_and_drop(source, target)`

### Waits

Examples include:

- `implicitly_wait(time_to_wait)`
- `WebDriverWait(driver, timeout)`

### Cookie Handling

Examples include:

- `get_cookies()`
- `add_cookie(cookie_dict)`

### Options Management

Examples include:

- `add_argument(argument)`
- `set_headless(headless=True)`

### Service and Driver Management

Examples include:

- `Service(executable_path)`
- `Remote`

### Browser Management

Examples include:

- `get_log(log_type)`
- `log_types`

### Shadow DOM Interaction

Examples include:

- `find_element(By.CSS_SELECTOR, 'selector').shadow_root`

## Running Tests

To run all tests using pytest, use the following command:

```bash
pytest
```

You can also run individual test files:
```bash
pytest test_webdriver_methods.py
```

## Examples

Each example is organized in separate test files under the `tests` directory. The files are named according to the feature they demonstrate. Here’s a brief overview of the examples provided:

- `test_webdriver_methods.py`: Demonstrates various WebDriver methods such as `get()`, `close()`, `maximize_window()`, and `get_screenshot_as_file()`.
- `test_webelement_methods.py`: Covers WebElement methods including `click()`, `send_keys()`, `get_attribute()`, and `is_displayed()`.
- `test_locating_elements.py`: Shows how to locate elements using methods like `find_element(By.ID, value)` and `find_elements(By.CSS_SELECTOR, value)`.
- `test_navigation_methods.py`: Includes examples of navigation methods such as `switch_to.window()` and `switch_to.frame()`.
- `test_alert_handling.py`: Contains examples of handling alerts with `accept()` and `dismiss()`.
- `test_action_chains.py`: Demonstrates the use of action chains for mouse and keyboard actions, including `move_to_element()` and `drag_and_drop()`.
- `test_waits.py`: Shows how to use implicit and explicit waits with `implicitly_wait()` and `WebDriverWait()`.
- `test_cookie_handling.py`: Includes examples for managing cookies with `get_cookies()` and `add_cookie()`.
- `test_options_management.py`: Covers browser options management with `add_argument()` and `set_headless()`.
- `test_service_driver_management.py`: Demonstrates the use of `Service()` and `Remote`.
- `test_browser_management.py`: Includes examples for retrieving browser logs with `get_log()`.
- `test_shadow_dom_interaction.py`: Shows how to interact with Shadow DOM elements using `find_element(By.CSS_SELECTOR, 'selector').shadow_root`.

Feel free to explore these examples to see how different Selenium features can be implemented using pytest.

## Contributing

Contributions are welcome! If you find an issue or want to add a new example, follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top-right of this page.
2. **Clone your fork**: 

    ```bash
    git clone https://github.com/ronikrawat/selenium-pytest-examples.git
    cd selenium-pytest-examples
    ```

3. **Create a new branch**: 

    ```bash
    git checkout -b feature/your-feature
    ```

4. **Make your changes** and commit them:

    ```bash
    git add .
    git commit -m "Add new example for feature X"
    ```

5. **Push to your fork**:

    ```bash
    git push origin feature/your-feature
    ```

6. **Create a pull request**: Go to the repository on GitHub and click "Compare & pull request".

