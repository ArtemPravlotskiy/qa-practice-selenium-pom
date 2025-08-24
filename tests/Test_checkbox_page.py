from pages.Checkbox_page import CheckboxPage

class TestCheckboxPage:

    def setup_method(self):
        self.checkbox_page = CheckboxPage(self.driver)

    def test_open_from_nav_bar(self):
        self.checkbox_page.open()
        self.checkbox_page.open_current_page_from_nav(self.checkbox_page.CHECKBOX_LINK_LOCATOR)
        assert self.checkbox_page.driver.current_url == self.checkbox_page.PAGE_URL, \
            "Wrong link in nav bar for 'Checkbox'"

    def test_there_is_one_single_checkbox(self):
        self.checkbox_page.open()
        num = len(self.checkbox_page.get_all_checkboxes())
        assert num == 1, \
            f"On page {self.checkbox_page.driver.current_url} not one checkbox, there are {num}"

    def test_label_single_checkbox(self):
        self.checkbox_page.open()
        expect = "select me or not"
        label = self.checkbox_page.get_checkbox_label(self.checkbox_page.SINGLE_CHECKBOX_LOCATOR)
        assert label == expect, \
            f"Wrong checkbox label, expected: {expect}, actual: {label}"

    def test_select_checkbox_result(self):
        self.checkbox_page.open()
        self.checkbox_page.select_checkbox(self.checkbox_page.SINGLE_CHECKBOX_LOCATOR)
        self.checkbox_page.click_submit_button()
        assert self.checkbox_page.is_element_visible(self.checkbox_page.RESULT_BOX_LOCATOR), \
            f"There is no result box after submit selected single checkbox"

    def test_no_select_checkbox_result(self):
        self.checkbox_page.open()
        self.checkbox_page.click_submit_button()
        assert not self.checkbox_page.is_element_visible(self.checkbox_page.RESULT_BOX_LOCATOR), \
            f"There should no result box after submit no selected single checkbox"

    def test_no_select_checkboxes_result(self):
        self.checkbox_page.open()
        self.checkbox_page.open_checkboxes()
        self.checkbox_page.click_submit_button()
        assert not self.checkbox_page.is_element_visible(self.checkbox_page.RESULT_BOX_LOCATOR), \
            f"There should no result box after submit no selected checkboxes"

    def test_label_of_result_with_checkboxes(self):
        self.checkbox_page.open()
        self.checkbox_page.open_checkboxes()
        self.checkbox_page.select_checkbox(self.checkbox_page.CHECKBOX_ONE_LOCATOR)
        self.checkbox_page.select_checkbox(self.checkbox_page.CHECKBOX_THREE_LOCATOR)
        self.checkbox_page.click_submit_button()
        result = self.checkbox_page.find(self.checkbox_page.RESULT_TEXT_LOCATOR).text
        assert "one" in result and "three" in result, \
            f"Wrong result text: {result}, with locator: {self.checkbox_page.RESULT_TEXT_LOCATOR}, Should be: 'one, three'"