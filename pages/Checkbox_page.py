import logging

from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class CheckboxPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"

    """Locators"""
    CHECKBOX_LINK_LOCATOR = ("link text", "Checkbox")
    SINGLE_CHECKBOX_LOCATOR = ("id", "id_checkbox_0")
    SUBMIT_BUTTON_LOCATOR = ("id", "submit-id-submit")
    RESULT_BOX_LOCATOR = ("id", "result")
    RESULT_TEXT_LOCATOR = ("id", "result-text")
    SINGLE_CHECKBOX_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    CHECKBOXES_LINK_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    CHECKBOX_ONE_LOCATOR = ("id", "id_checkboxes_0")
    CHECKBOX_TWO_LOCATOR = ("id", "id_checkboxes_1")
    CHECKBOX_THREE_LOCATOR = ("id", "id_checkboxes_2")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def open_single_checkbox(self):
        self.find(self.SINGLE_CHECKBOX_LINK_LOCATOR).click()
        logger.info("Go to single checkbox page")

    def open_checkboxes(self):
        self.find(self.CHECKBOXES_LINK_LOCATOR).click()
        logger.info("Go to checkboxes page")

    def get_all_checkboxes(self):
        elements = self.driver.find_elements("css selector", "input[type='checkbox']")
        logger.info(f"Found {len(elements)} checkboxes")
        return elements

    def get_checkbox_label(self, locator):
        label = self.find(locator).get_attribute("value")
        if label is None:
            label = self.find(locator).text
        logger.info(f"Label of checkbox {self.SINGLE_CHECKBOX_LOCATOR} is {label}")
        return label

    def click_submit_button(self):
        self.click_with_wait(self.SUBMIT_BUTTON_LOCATOR)

    def is_there_result(self):
        return self.is_element_visible(self.RESULT_BOX_LOCATOR)

    def get_result_label(self):
        if self.is_there_result():
            text = self.find(self.RESULT_TEXT_LOCATOR).text
            logger.info(f"Result text: {text}")
            return text
        logger.error(f"There is no result in DOM")
        return None

    def select_checkbox(self, locator):
        check = self.find(locator)
        check.click()
        logger.info(f"Select checkbox: {locator}")