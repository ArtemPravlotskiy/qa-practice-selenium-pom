import time

import pytest

from pages.Alert_page import AlertPage

class TestAlertPage:

    def setup_method(self):
        self.alert_page = AlertPage(self.driver)

    def test_open_from_nav_bar(self):
        self.alert_page.open()
        self.alert_page.open_current_page_from_nav(self.alert_page.ALERTS_LINK_LOCATOR)
        assert self.alert_page.driver.current_url == self.alert_page.PAGE_URL, \
            "Wrong link in nav bar for 'Alerts'"

    def test_alert(self):
        self.alert_page.open()
        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()

        # correct text
        assert alert.text == "I am an alert!", f"Wrong alert text, {alert}"

        # correct type
        with pytest.raises(Exception):
            alert.send_keys("test")

        # alert close after click OK
        alert.accept()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()


    def test_confirm(self):
        self.alert_page.open()
        self.alert_page.switch_type_page(self.alert_page.CONFIRM_LOCATOR)
        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()

        # correct text
        assert alert.text == "Select Ok or Cancel", f"Wrong alert text, {alert}"

        # correct type
        with pytest.raises(Exception):
            alert.send_keys("test")

        # alert close after click OK
        alert.accept()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()

        assert self.alert_page.find(self.alert_page.RESULT_TEXT_LOCATOR).text == "Ok", \
            f"Wrong answer of confirm result (Ok)"

        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()
        alert.dismiss()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()
        assert self.alert_page.find(self.alert_page.RESULT_TEXT_LOCATOR).text == "Cancel", \
            f"Wrong answer of confirm result (Cancel)"


    def test_promt(self):
        self.alert_page.open()
        self.alert_page.switch_type_page(self.alert_page.PROMPT_LOCATOR)
        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()

        # correct text
        assert alert.text == "Please enter some text", f"Wrong alert text, {alert}"

        # close after click OK
        alert.accept()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()
        assert self.alert_page.find(self.alert_page.RESULT_TEXT_LOCATOR).text == "You entered nothing", \
            f"Wrong empty ok prompt logic"

        # close after click Cancel
        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()
        alert.dismiss()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()
        assert self.alert_page.find(self.alert_page.RESULT_TEXT_LOCATOR).text == "You canceled the prompt", \
            f"Wrong cancel prompt logic"

        # usual test
        self.alert_page.click_button()
        alert = self.alert_page.switch_to_alert()
        alert.send_keys("test")
        alert.accept()
        with pytest.raises(Exception):
            self.alert_page.switch_to_alert()
        assert self.alert_page.find(self.alert_page.RESULT_TEXT_LOCATOR).text == "test", \
            f"Wrong cancel prompt logic"