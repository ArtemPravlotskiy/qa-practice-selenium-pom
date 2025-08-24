import logging
from pages.Base_page import BasePage
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)

class InputPage(BasePage):

    PAGE_URL = "https://www.qa-practice.com/elements/input/simple"

    """Locators"""
    INPUT_LINK_LOCATOR = ("link text", "Inputs")
    TEXT_INPUT_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    EMAIL_FIELD_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    PASSWORD_FIELD_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(3) > a")
    TEXT_INPUT_LOCATOR = ("id", "id_text_string")
    EMAIL_INPUT_LOCATOR = ("id", "id_email")
    PASSWORD_INPUT_LOCATOR = ("id", "id_password")
    RESULT_LOCATOR = ("id", "result-text")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def open_text_input(self):
        self.click_with_wait(self.TEXT_INPUT_LINK_LOCATOR)
        logger.info(f"Click on element {self.TEXT_INPUT_LINK_LOCATOR} at {self.driver.current_url}")

    def open_email_field(self):
        self.click_with_wait(self.EMAIL_FIELD_LINK_LOCATOR)
        logger.info(f"Click on element {self.EMAIL_FIELD_LINK_LOCATOR} at {self.driver.current_url}")

    def open_password_field(self):
        self.click_with_wait(self.PASSWORD_FIELD_LINK_LOCATOR)
        logger.info(f"Click on element {self.PASSWORD_FIELD_LINK_LOCATOR} at {self.driver.current_url}")

    def input_text_to_field(self, locator, value: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(value + Keys.ENTER)
        logger.info(f"Input '{value}' into element {locator} on {self.driver.current_url}")

    def input_text(self, line: str):
        self.input_text_to_field(self.TEXT_INPUT_LOCATOR, line)

    def input_email(self, line: str):
        self.input_text_to_field(self.EMAIL_INPUT_LOCATOR, line)

    def input_password(self, line: str):
        self.input_text_to_field(self.PASSWORD_INPUT_LOCATOR, line)

    def check_result(self, key: str) -> bool:
        if self.is_element_visible(self.RESULT_LOCATOR):
            if self.find(self.RESULT_LOCATOR).text == key:
                logger.info("Check success")
                return True
        logger.info("Check wrong")
        return False