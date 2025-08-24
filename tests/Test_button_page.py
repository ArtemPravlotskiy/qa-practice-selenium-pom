from pages.Button_page import ButtonPage

class TestButtonPage:

    def setup_method(self):
        self.button_page = ButtonPage(self.driver)

    def test_open_from_nav_bar(self):
        self.button_page.open()
        self.button_page.open_current_page_from_nav(self.button_page.BUTTONS_LINK_LOCATOR)
        assert self.button_page.driver.current_url == "https://www.qa-practice.com/elements/button/simple", \
            "Wrong link in nav bar for 'Buttons'"

    def test_simple_button(self):
        self.button_page.open()
        self.button_page.find(self.button_page.SIMPLE_BUTTON_LOCATOR).click()
        assert self.button_page.is_element_visible(self.button_page.RESULT_LOCATOR), \
            "Error click simple button"

    def test_like_button(self):
        self.button_page.open()
        self.button_page.find(self.button_page.LIKE_BUTTON_LINK_LOCATOR).click()
        self.button_page.find(self.button_page.LIKE_BUTTON_LOCATOR).click()
        assert self.button_page.is_element_visible(self.button_page.RESULT_LOCATOR), \
            "Error click like button"

    def test_disabled_button(self):
        self.button_page.open()
        self.button_page.find(self.button_page.DISABLED_BUTTON_LINK_LOCATOR).click()
        assert self.button_page.find(self.button_page.DISABLED_BUTTON_LOCATOR).get_attribute("disabled") == "true", \
            "Button was enabled from the start"

        self.button_page.find(self.button_page.SELECT_ENABLE_LOCATOR).click()
        """Button should enable immediately"""
        self.button_page.driver.find_element(*self.button_page.DISABLED_BUTTON_LOCATOR).click()

        assert self.button_page.is_element_visible(self.button_page.RESULT_LOCATOR), \
            "Error click disable button"