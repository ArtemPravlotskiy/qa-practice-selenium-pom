import logging
from pages.Base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

logger = logging.getLogger(__name__)

class DragAndDropPage(BasePage):

    PAGE_URL = "https://www.qa-practice.com/elements/dragndrop/boxes"

    """Locators"""
    DRAG_AND_DROP_LINK_LOCATOR = ("link text", "Drag and Drop")
    DRAGGABLE_LOCATOR = ("id", "rect-draggable")
    DROPPABLE_LOCATOR = ("id", "rect-droppable")
    DROPPABLE_TEXT_LOCATOR = ("id", "text-droppable")
    IMG_LOCATOR = ("css selector", 'img[src="/static/home/smile.png"]')
    DROPPABLE_1_LOCATOR = ("id", "rect-droppable1")
    DROPPABLE_2_LOCATOR = ("id", "rect-droppable2")
    SMILE_LOCATOR = ("css selector", "#content > ul > li:nth-child(2) > a")
    TEXT_1_LOCATOR = ("css selector", "#rect-droppable1 > p")
    TEXT_2_LOCATOR = ("css selector", "#rect-droppable2 > p")

    def open(self):
        self.driver.get(self.PAGE_URL)
        logger.info(f"Open page: {self.PAGE_URL}")

    def go_to_smile(self):
        self.click_with_wait(self.SMILE_LOCATOR)
        logger.info(f"Open page smile")

    def get_action_chains(self):
        logger.info("Create action chain")
        return ActionChains(self.driver)

    def drag_and_drop(self, target, aim):
        action = self.get_action_chains()
        action.drag_and_drop(self.find(target), self.find(aim)).perform()
        logger.info(f"Drag: {target}, and drop in aim: {aim}")


    def get_text(self, locator):
        text = self.find(locator).text
        logger.info(f"Text from locator ({locator}), is: {text}")
        return text

    def is_smile_text_visible(self, i: int):
        locator = self.TEXT_1_LOCATOR if i == 1 else self.TEXT_2_LOCATOR
        return self.is_element_visible(locator)