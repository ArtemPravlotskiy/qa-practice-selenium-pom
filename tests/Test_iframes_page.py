import pytest

from pages.Iframes_page import IframesPage

class TestIframePage:

    def setup_method(self):
        self.iframe_page = IframesPage(self.driver)

    def test_open_from_nav_bar(self):
        self.iframe_page.open()
        self.iframe_page.open_current_page_from_nav(self.iframe_page.IFRAMES_LINK_LOCATOR)
        assert self.iframe_page.driver.current_url == self.iframe_page.PAGE_URL, \
            "Wrong link in nav bar for 'Select'"

    def test_iframe(self):
        self.iframe_page.open()
        self.iframe_page.switch_to_iframe()
        assert self.iframe_page.find(self.iframe_page.UNDER_FRAME_LOCATOR), "Do not switch to iframe"
        self.iframe_page.switch_to_main()
        with pytest.raises(Exception):
            self.iframe_page.find(self.iframe_page.UNDER_FRAME_LOCATOR)
        assert self.iframe_page.find(self.iframe_page.HOMEPAGE_BUTTON_LOCATOR), "Do not switch to main"