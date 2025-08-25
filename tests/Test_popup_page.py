import logging

from pages.Popup_page import PopUpPage

class TestPopupPage:

    def setup_method(self):
        self.popup_page = PopUpPage(self.driver)

    def test_open_from_nav_bar(self):
        self.popup_page.open()
        self.popup_page.open_current_page_from_nav(self.popup_page.POP_UP_LINK_LOCATOR)
        assert self.popup_page.driver.current_url == self.popup_page.PAGE_URL, \
            "Wrong link in nav bar for 'Pop-Up'"

    def test_send_none(self):
        self.popup_page.open()
        self.popup_page.open_popup()
        self.popup_page.send_popup()
        expect = "None"
        actual = self.popup_page.get_result_text()
        assert expect == actual, f"Wrong result, expect: {expect}, actual: {actual}"

    def test_send_checkbox(self):
        self.popup_page.open()
        self.popup_page.open_popup()
        self.popup_page.select_checkbox()
        self.popup_page.send_popup()
        expect = "select me or not"
        actual = self.popup_page.get_result_text()
        assert expect == actual, f"Wrong result, expect: {expect}, actual: {actual}"

    def test_frame_popup_right(self):
        self.popup_page.open()
        self.popup_page.go_to_iframe()
        self.popup_page.open_popup()
        text = self.popup_page.copy_text()
        self.popup_page.check_popup()
        luck = self.popup_page.check_text(text)
        assert luck, "Error checking text"

    def test_iframe_empty_check(self):
        self.popup_page.open()
        self.popup_page.go_to_iframe()
        self.popup_page.open_popup()
        self.popup_page.check_popup()
        luck = self.popup_page.check_text("test")
        assert not luck, "Error checking text"