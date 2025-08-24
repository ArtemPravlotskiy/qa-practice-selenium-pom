import os.path
from datetime import datetime
import logging

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

def pytest_configure(config):
    level = logging.DEBUG if config.getoption("debug") else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("test.log", mode="w", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logging.info("=== START TEST SESSION ===")

def pytest_addoption(parser):
    """Params for pytest command line"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Available browsers: chrome(default), firefox, edge, all")
    parser.addoption("--parallel", action="store_true", default=False,
                     help="Run tests in parallel (pytest-xdist)")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run in headless mode")
    parser.addoption("--debug_logs", action="store_true", default=False,
                     help="Enable debug logging")


@pytest.fixture(autouse=True)
def driver(request):
    browser = request.param
    headless = request.config.getoption("headless")
    # cache_manager = DriverCacheManager(root_dir="./.wdm_cache")

    if browser == "chrome":
        logging.debug("Start creation Chrome WebDriver")
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless=new")
            logging.debug("Turn on headless mode")

        # service = ChromeService(executable_path=ChromeDriverManager(cache_manager=cache_manager).install())
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        logging.debug("Start creation Firefox WebDriver")
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless")
            logging.debug("Turn on headless mode")

        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        logging.debug("Start creation Edge WebDriver")
        options = webdriver.EdgeOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless=new")
            logging.debug("Turn on headless mode")

        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    else:
        logging.error("Unsupported browser selected")
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield driver
    driver.quit()

def pytest_generate_tests(metafunc):
    """What browsers should be tested"""
    if "driver" in metafunc.fixturenames:
        browser_option = metafunc.config.getoption("browser")
        parallel = metafunc.config.getoption("parallel")

        if browser_option == "all":
            browsers = ["chrome", "firefox", "edge"]
        else:
            browsers = [browser_option]

        metafunc.parametrize("driver", browsers, indirect=True)

        if parallel and browser_option == "all":
            print(f"\n[INFO] Parallel mode ON. Use: pytest -n {len(browsers)}")

ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            # screenshot
            screenshot_path = os.path.join(ARTIFACTS_DIR, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            logging.error(f"Screenshot save: {screenshot_path}")

            # HTML
            html_path = os.path.join(ARTIFACTS_DIR, f"{test_name}_{timestamp}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            logging.error(f"HTML save: {html_path}")

            # Browser logs
            try:
                log_path = os.path.join(ARTIFACTS_DIR, f"{test_name}_{timestamp}.log")
                logs = driver.get_log("browser")
                with open(log_path, "w", encoding="utf-8") as f:
                    for entry in logs:
                        f.write(f"{entry['level']} - {entry['message']}\n")
                logging.error(f"Browser logs save: {log_path}")
            except Exception as e:
                logging.warning(f"There is not browser logs: {e}")