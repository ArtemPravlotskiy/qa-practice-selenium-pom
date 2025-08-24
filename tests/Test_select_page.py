from pages.Select_page import SelectPage
import pytest

class TestSelectPage:

    def setup_method(self):
        self.select_page = SelectPage(self.driver)

    def test_open_from_nav_bar(self):
        self.select_page.open()
        self.select_page.open_current_page_from_nav(self.select_page.SELECT_LINK_LOCATOR)
        assert self.select_page.driver.current_url == self.select_page.PAGE_URL, \
            "Wrong link in nav bar for 'Select'"

    def test_field_name_single_select(self):
        self.select_page.open()
        expect = "Choose language"
        actual = self.select_page.get_label_text(self.select_page.LABEL_SELECT_LOCATOR)
        assert expect == actual, f"Wrong field name, expect: {expect}, actual: {actual}."

    def test_select_has_required(self):
        self.select_page.open()
        assert self.select_page.find(self.select_page.SELECT_LOCATOR). \
                   get_attribute("required") == "true", \
            f"Selector {self.select_page.SELECT_LOCATOR} is not required"

    def test_empty_form(self):
        self.select_page.open()
        self.select_page.click_submit_button()
        assert not self.select_page.is_element_visible(self.select_page.RESULT_TEXT_LOCATOR), \
            f"Able to send an empty form"

    @pytest.mark.parametrize("language", [
        "Python",
        "JavaScript",
        "Java"
    ])
    def test_send_form(self, language):
        self.select_page.open()
        select = self.select_page.get_selector(self.select_page.SELECT_LOCATOR)
        select.select_by_visible_text(language)
        self.select_page.click_submit_button()
        result = self.select_page.get_result_text()
        assert language == result, \
            f"Error selector logic: {self.select_page.SELECT_LOCATOR}"

    def test_field_name_multi_select(self):
        self.select_page.open()
        self.select_page.open_multi_select()
        expect1 = "Choose the place you want to go"
        expect2 = "Choose how you want to get there"
        expect3 = "Choose when you want to go"
        actual = self.select_page.get_label_text(self.select_page.LABEL_SELECT1_LOCATOR)
        assert expect1 == actual, f"Wrong field name, expect: {expect1}, actual: {actual}."
        actual = self.select_page.get_label_text(self.select_page.LABEL_SELECT2_LOCATOR)
        assert expect2 == actual, f"Wrong field name, expect: {expect2}, actual: {actual}."
        actual = self.select_page.get_label_text(self.select_page.LABEL_SELECT3_LOCATOR)
        assert expect3 == actual, f"Wrong field name, expect: {expect3}, actual: {actual}."

    def test_multi_select_has_required(self):
        self.select_page.open()
        self.select_page.open_multi_select()
        assert self.select_page.find(self.select_page.FIRST_SELECT_LOCATOR). \
                   get_attribute("required") == "true", \
            f"Selector {self.select_page.SELECT_LOCATOR} is not required"
        assert self.select_page.find(self.select_page.SECOND_SELECT_LOCATOR). \
                   get_attribute("required") == "true", \
            f"Selector {self.select_page.SELECT_LOCATOR} is not required"
        assert self.select_page.find(self.select_page.THIRD_SELECT_LOCATOR). \
                   get_attribute("required") == "true", \
            f"Selector {self.select_page.SELECT_LOCATOR} is not required"

    def test_empty_multi_form(self):
        self.select_page.open()
        self.select_page.open_multi_select()
        self.select_page.click_submit_button()
        assert not self.select_page.is_element_visible(self.select_page.RESULT_TEXT_LOCATOR), \
            f"Able to send an empty multi form"

    @pytest.mark.parametrize("first, second, third", [
        ("Sea", "Car", "Today"),
        ("Old town", "Bus", "Tomorrow"),
        ("Restaurant", "Air", "Next week"),
    ])
    def test_send_multi_form(self, first, second, third):
        self.select_page.open()
        self.select_page.open_multi_select()
        select1 = self.select_page.get_selector(self.select_page.FIRST_SELECT_LOCATOR)
        select1.select_by_visible_text(first)
        select2 = self.select_page.get_selector(self.select_page.SECOND_SELECT_LOCATOR)
        select2.select_by_visible_text(second)
        select3 = self.select_page.get_selector(self.select_page.THIRD_SELECT_LOCATOR)
        select3.select_by_visible_text(third)
        self.select_page.click_submit_button()
        result = self.select_page.get_result_text()
        expect_result = "to go by " + second.lower() + " to the " + first.lower() + " " + third.lower()
        assert expect_result == result, \
            f"Error selector logic: {self.select_page.SELECT_LOCATOR}. Expect: {expect_result}, result: {result}"