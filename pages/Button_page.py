import logging
from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class ButtonPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/button/simple"
    BUTTON_LABEL = "Click"

    """Locators"""
    SIMPLE_BUTTON_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    LIKE_BUTTON_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    DISABLED_BUTTON_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(3) > a")
    SIMPLE_BUTTON_LOCATOR = ("id", "submit-id-submit")
    LIKE_BUTTON_LOCATOR = ("css selector", ".a-button")
    DISABLED_BUTTON_LOCATOR = ("id", "submit-id-submit")
    SELECT_ENABLE_LOCATOR = ("css selector", "option[value='enabled']")
    RESULT_LOCATOR = ("id", "result")
    BUTTONS_LINK_LOCATOR = ("link text", "Buttons")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def choose_select_enable(self):
        self.find(self.SELECT_ENABLE_LOCATOR).click()
        logger.info(f"Choose enable select on page: {self.driver.current_url}")

    def check_element_label(self, locator, label):
        element = self.find(locator)
        text = element.text
        if text == label:
            logger.info(f"Element: {locator}, has right label: {label}")
            return True
        logger.info(f"Element: {locator}, should had label: {label}, but it has: {text}")
        return False