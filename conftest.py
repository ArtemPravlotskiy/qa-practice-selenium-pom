import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """Params for pytest command line"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Available browsers: chrome(default), firefox, edge, all")
    parser.addoption("--parallel", action="store_true", default=False,
                     help="Run tests in parallel (pytest-xdist)")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.param
    headless = request.config.getoption("headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless=new")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless")

        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--window-size=1920,1080")

        if headless:
            options.add_argument("--headless=new")

        service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)

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