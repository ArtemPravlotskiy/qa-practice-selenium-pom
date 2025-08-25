import logging
from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class AlertPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/alert/alert"

    """Locators"""
    ALERTS_LINK_LOCATOR = ("link text", "Alerts")
    BUTTON_LOCATOR = ("class name", "a-button")
    ALERT_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    CONFIRM_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    PROMPT_LOCATOR = ("css selector", "#content > ul > li:nth-child(3) > a")
    RESULT_TEXT_LOCATOR = ("id", "result-text")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def click_button(self):
        self.click_with_wait(self.BUTTON_LOCATOR)

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        logger.info(f"Switch to alert: {alert}")
        return alert

    def switch_type_page(self, locator):
        self.click_with_wait(locator)
        logger.info(f"Switch type page by click locator: {locator}")