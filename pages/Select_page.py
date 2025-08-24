import logging
from selenium.webdriver.support.select import Select

from pages.Base_page import BasePage

logger = logging.getLogger(__name__)

class SelectPage(BasePage):
    PAGE_URL = "https://www.qa-practice.com/elements/select/single_select"

    """Locators"""
    SELECT_LINK_LOCATOR = ("link text", "Select")
    SINGLE_SELECT_LOCATOR = ("css selector", "#content > ul > li:nth-child(1) > a")
    MULTI_SELECT_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    SELECT_LOCATOR = ("id", "id_choose_language")
    SUBMIT_BUTTON_LOCATOR = ("id", "submit-id-submit")
    LABEL_SELECT_LOCATOR = ("class name", "form-label")
    LABEL_SELECT1_LOCATOR = ("css selector", "#div_id_choose_the_place_you_want_to_go > label")
    LABEL_SELECT2_LOCATOR = ("css selector", "#div_id_choose_how_you_want_to_get_there > label")
    LABEL_SELECT3_LOCATOR = ("css selector", "#div_id_choose_when_you_want_to_go > label")
    FIRST_SELECT_LOCATOR = ("id", "id_choose_the_place_you_want_to_go")
    SECOND_SELECT_LOCATOR = ("id", "id_choose_how_you_want_to_get_there")
    THIRD_SELECT_LOCATOR = ("id", "id_choose_when_you_want_to_go")
    RESULT_TEXT_LOCATOR = ("id", "result-text")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def open_single_select(self):
        self.find(self.SINGLE_SELECT_LOCATOR).click()
        logger.info("Go to single select page")

    def open_multi_select(self):
        self.find(self.MULTI_SELECT_LOCATOR).click()
        logger.info("Go to multi select page")

    def get_label_text(self, locator):
        text = self.find(locator).text
        logger.info(f"Label text for locator: {locator}, is - '{text}'")
        return text[:-1]

    def get_selector(self, locator):
        selector = self.find(locator)
        logger.info(f"Found selector with id: {selector.get_attribute('id')}")
        return Select(selector)

    def click_submit_button(self):
        self.click_with_wait(self.SUBMIT_BUTTON_LOCATOR)

    def get_result_text(self):
        result = self.find(self.RESULT_TEXT_LOCATOR)
        logger.info(f"Result text: {result.text}")
        return result.text