import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    """Fixture to provide WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the driver from the test function
        driver = getattr(item, '_driver', None)
        if driver:
            # Create screenshots directory if it doesn't exist
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            # Take screenshot
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report
            if hasattr(report, 'extra'):
                report.extra = getattr(report, 'extra', [])
                report.extra.append({
                    'name': 'Screenshot',
                    'format': 'image',
                    'content': screenshot_path,
                    'mime_type': 'image/png'
                })
