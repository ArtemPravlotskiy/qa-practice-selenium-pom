from pages.Main_page import MainPage

class TestMainPage:

    def setup_method(self):
        self.main_page = MainPage(self.driver)

    def test_title(self):
        self.main_page.open()
        expected_title = "Home Page | QA Practice"
        title = self.main_page.get_page_title()
        assert title == expected_title, "Wrong page title"

    def test_content_links(self):
        self.main_page.open()
        expected_links = [
            "/elements/input/simple",
            "/elements/button/simple",
            "/elements/checkbox/single_checkbox",
            "/elements/textarea/single",
            "/elements/select/single_select"
        ]
        links = self.main_page.get_content_urls()
        assert all(any(expected in link for link in links) for expected in expected_links), \
            f"Wrong content links.\nExpected: {expected_links}\nGot: {links}"