import logging
from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class IframesPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/iframe/iframe_page"

    """Locators"""
    IFRAMES_LINK_LOCATOR = ("link text", "Iframes")
    IFRAME_LOCATOR = ("css selector", "#content > iframe")
    UNDER_FRAME_LOCATOR = ("css selector", "body > div > main > section > div > div > p:nth-child(3) > a.btn.btn-primary.my-2")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.find(self.IFRAME_LOCATOR))
        logger.info("Switch to iframe")

    def switch_to_main(self):
        self.driver.switch_to.default_content()
        logger.info("Switch to default frame")