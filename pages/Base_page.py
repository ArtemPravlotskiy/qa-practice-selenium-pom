import logging

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class BasePage:

    HOMEPAGE_BUTTON_LOCATOR = ("class name", "active")
    SUB_MENU_LOCATOR = ("class name", "caret")
    # INPUT_LINK_LOCATOR = ("link text", "Inputs")
    # BUTTONS_LINK_LOCATOR = ("link text", "Buttons")
    # CHECKBOX_LINK_LOCATOR = ("link text", "Checkbox")
    # SELECT_LINK_LOCATOR = ("link text", "Select")
    # NEW_TAB_LINK_LOCATOR = ("link text", "New tab")
    # TEXT_AREA_LINK_LOCATOR = ("link text", "Text area")
    # ALERTS_LINK_LOCATOR = ("link text", "Alerts")
    # DRAG_AND_DROP_LINK_LOCATOR = ("link text", "Drag and Drop")
    # IFRAMES_LINK_LOCATOR = ("link text", "Iframes")
    # POP_UP_LINK_LOCATOR = ("link text", "Pop-Up")

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
                EC.presence_of_element_located(locator)
            )
            logger.info(f"The element was found: {locator}")
            return element
        except TimeoutException:
            logger.error(f"The element was NOT found in {self.timeout} seconds: {locator}")
            raise

    def click_with_wait(self, locator):
        """Click with waiting for {timeout} seconds"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logger.info(f"Click on an element: {locator}")
        except TimeoutException:
            logger.error(f"The element is not clickable: {locator}")
            raise

    def homepage(self):
        """Go to homepage"""
        self.click_with_wait(self.HOMEPAGE_BUTTON_LOCATOR)
        logger.info(f"Go to homepage by click: {self.HOMEPAGE_BUTTON_LOCATOR}")

    def open_navigation_sub_menu(self):
        """Open navigation sub-menu"""
        self.click_with_wait(self.SUB_MENU_LOCATOR)
        logger.info(f"Open navigation sub-menu by click: {self.SUB_MENU_LOCATOR}")

    def is_element_visible(self, locator):
        """Check visibility of the element"""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Element is NOT visible: {locator}")
            return False

    def get_page_title(self) -> str:
        """Get current page title"""
        title = self.driver.title
        logger.info(f"Current page title: {title}")
        return title