from pages.Newtab_page import NewtabPage

class TestNewtabPage:

    def setup_method(self):
        self.newtab_page = NewtabPage(self.driver)

    def test_open_from_nav_bar(self):
        self.newtab_page.open()
        self.newtab_page.open_current_page_from_nav(self.newtab_page.NEW_TAB_LINK_LOCATOR)
        assert self.newtab_page.driver.current_url == self.newtab_page.PAGE_URL, \
            "Wrong link in nav bar for 'New tab'"

    def test_open_tab_by_link(self):
        self.newtab_page.open()
        url = self.newtab_page.get_current_url()
        self.newtab_page.click_link()
        assert self.newtab_page.get_current_url() == url, "Page should open in new tab"
        self.newtab_page.switch_to_new_tab()
        new_url = self.newtab_page.get_current_url()
        assert new_url == self.newtab_page.OPEN_PAGE_URL, \
            f"Expected new url: {self.newtab_page.OPEN_PAGE_URL}, actual: {new_url}"

    def test_open_tab_by_button(self):
        self.newtab_page.open()
        self.newtab_page.open_new_tab_button()
        url = self.newtab_page.get_current_url()
        self.newtab_page.click_button()
        assert self.newtab_page.get_current_url() == url, "Page should open in new tab"
        self.newtab_page.switch_to_new_tab()
        new_url = self.newtab_page.get_current_url()
        assert new_url == self.newtab_page.OPEN_PAGE_URL, \
            f"Expected new url: {self.newtab_page.OPEN_PAGE_URL}, actual: {new_url}"