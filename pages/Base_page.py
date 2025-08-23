import logging

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class BasePage:

    HOMEPAGE_BUTTON_LOCATOR = ("class name", "active")
    SUB_MENU_LOCATOR = ("class name", "sub-menu")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def open(self):
        """Method must be implemented in the child class"""
        raise NotImplementedError("The open() method must be implemented in the child class.")

    def find(self, locator):
        """Safe search with expectation"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(*locator)
            )
            logger.info(f"The element was found: {locator}")
            return element
        except TimeoutException:
            logger.error("The element was NOT found in {self.timeout} seconds: {locator}")
            raise

    def click_with_wait(self, locator):
        """Click with waiting for {timeout} seconds"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(*locator)
            )
            element.click()
            logger.info(f"Click on an element: {locator}")
        except TimeoutException:
            logger.error(f"The element is not clickable: {locator}")
            raise

    def homepage(self):
        """Go to homepage"""
        self.driver.find_element(*self.HOMEPAGE_BUTTON_LOCATOR).click()
        logger.info(f"Go to homepage by click: {self.HOMEPAGE_BUTTON_LOCATOR}")

    def open_sub_menu(self):
        """Open navigation sub-menu"""
        self.driver.find_element(*self.SUB_MENU_LOCATOR).click()
        logger.info(f"Open navigation sub-menu by click: {self.SUB_MENU_LOCATOR}")

    # TODO: this
    def is_element_visible(self, locator):
        """Check visibility of the element"""
