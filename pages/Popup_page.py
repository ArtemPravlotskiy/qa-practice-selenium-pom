import logging

from conftest import driver
from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class PopUpPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/popup/modal"

    """Locators"""
    POP_UP_LINK_LOCATOR = ("link text", "Pop-Up")
    MODAL_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    IFRAME_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    LAUNCH_BUTTON_LOCATOR = ("css selector", "#content > button")
    CHECKBOX_LOCATOR = ("id", "id_checkbox_0")
    CLOSE_BUTTON_LOCATOR = ("css selector", "#exampleModal > div > div > div.modal-footer > button.btn.btn-secondary")
    SEND_BUTTON_LOCATOR = ("css selector", "#exampleModal > div > div > div.modal-footer > button.btn.btn-primary")
    CHECK_BUTTON_LOCATOR = ("css selector", "#exampleModal > div > div > div > div.modal-footer > button.btn.btn-primary")
    POPUP_LOCATOR = ("id", "exampleModal")
    FRAME_LOCATOR = ("css selector", "#exampleModal > div > div > div > iframe")
    TEXT_TO_COPY_LOCATOR = ("css selector", "#text-to-copy")
    RESULT_TEXT_LOCATOR = ("id", "result-text")
    CHECK_FIELD_LOCATOR = ("id", "id_text_from_iframe")
    SUBMIT_BUTTON_LOCATOR = ("id", "submit-id-submit")
    CHECK_RESULT_LOCATOR = ("id", "check-result")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def go_to_iframe(self):
        self.click_with_wait(self.IFRAME_LOCATOR)
        logger.info("Open iframe sub-page")

    def open_popup(self):
        self.click_with_wait(self.LAUNCH_BUTTON_LOCATOR)
        logger.info("Launch pop up")

    def select_checkbox(self):
        self.click_with_wait(self.CHECKBOX_LOCATOR)
        logger.info("Click to checkbox")

    def close_popup(self):
        self.click_with_wait(self.CLOSE_BUTTON_LOCATOR)
        logger.info("Click to close")

    def send_popup(self):
        self.click_with_wait(self.SEND_BUTTON_LOCATOR)
        logger.info("Click to send")

    def check_popup(self):
        self.click_with_wait(self.CHECK_BUTTON_LOCATOR)
        logger.info("Click to send")

    def is_popup_visible(self):
        return self.is_element_visible(self.POPUP_LOCATOR)

    def copy_text(self):
        self.driver.switch_to.frame(self.find(self.FRAME_LOCATOR))
        text = self.find(self.TEXT_TO_COPY_LOCATOR).get_attribute("textContent")
        logger.info(f"Copy text: {text}")
        self.driver.switch_to.default_content()
        return text

    def get_result_text(self):
        text = self.find(self.RESULT_TEXT_LOCATOR).text
        logger.info(f"Result text: {text}")
        return text

    def check_text(self, text):
        self.find(self.CHECK_FIELD_LOCATOR).send_keys(text)
        self.click_with_wait(self.SUBMIT_BUTTON_LOCATOR)
        if self.find(self.CHECK_RESULT_LOCATOR).text == "Correct!":
            logger.info("Success check")
            return True
        logger.warning("Error check")
        return False