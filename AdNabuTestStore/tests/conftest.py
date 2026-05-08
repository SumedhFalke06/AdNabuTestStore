import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the driver from the test function
        driver = getattr(item, '_driver', None)
        if driver:

            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)


            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            driver.save_screenshot(screenshot_path)


            if hasattr(report, 'extra'):
                report.extra = getattr(report, 'extra', [])
                report.extra.append({
                    'name': 'Screenshot',
                    'format': 'image',
                    'content': screenshot_path,
                    'mime_type': 'image/png'
                })
