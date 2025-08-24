import logging

from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class MainPage(BasePage):

    PAGE_URL = "https://www.qa-practice.com/"

    """Locators"""

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def get_content_urls(self):
        elements = self.driver.find_elements("css selector", "#content li a")
        urls = [element.get_attribute("href") for element in elements]
        logger.info(f"Found {len(urls)} content links")
        return urls

