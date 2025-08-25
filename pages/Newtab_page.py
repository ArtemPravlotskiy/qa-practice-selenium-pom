import logging
from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class NewtabPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/new_tab/link"
    OPEN_PAGE_URL = "https://www.qa-practice.com/elements/new_tab/new_page"

    """Locators"""
    NEW_TAB_LINK_LOCATOR = ("link text", "New tab")
    NEW_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    NEW_BUTTON_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    LINK_LOCATOR = ("id", "new-page-link")
    BUTTON_LOCATOR = ("id", "new-page-button")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def open_new_tab_link(self):
        self.click_with_wait(self.NEW_LINK_LOCATOR)
        logger.info("Go to 'New tab link' page")

    def open_new_tab_button(self):
        self.click_with_wait(self.NEW_BUTTON_LOCATOR)
        logger.info("Go to 'New tab button' page")

    def click_link(self):
        self.click_with_wait(self.LINK_LOCATOR)
        logger.info("Open new tab by click the link")

    def click_button(self):
        self.click_with_wait(self.BUTTON_LOCATOR)
        logger.info("Open new tab by click the button")

    def get_current_url(self):
        logger.info(f"Current url is: '{self.driver.current_url}'")
        return self.driver.current_url

    def switch_to_new_tab(self, index: int = 1):
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[index])
            logger.info(f"Switched to tab {index}: {self.driver.current_url}")
        except IndexError:
            logger.error(f"Tab index {index} out of range. Available tabs: {len(handles)}")

    def close_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        logger.info(f"Close new tab, current tab is: {self.driver.current_url}")