from pages.Inputs_page import InputPage
import pytest

class TestInputPage:

    def setup_method(self):
        self.input_page = InputPage(self.driver)

    def test_open_from_nav_bar(self):
        self.input_page.open()
        self.input_page.open_current_page_from_nav(self.input_page.INPUT_LINK_LOCATOR)
        assert self.input_page.driver.current_url == "https://www.qa-practice.com/elements/input/simple", \
            "Wrong link in nav bar for 'Inputs'"

    def test_open_all_fields(self):
        self.input_page.open()
        self.input_page.open_email_field()
        assert self.input_page.driver.current_url == "https://www.qa-practice.com/elements/input/email", \
            "Wrong link in on button 'Email field'"

        self.input_page.open_password_field()
        assert self.input_page.driver.current_url == "https://www.qa-practice.com/elements/input/passwd", \
            "Wrong link in on button 'Password field'"

        self.input_page.open_text_input()
        assert self.input_page.driver.current_url == "https://www.qa-practice.com/elements/input/simple", \
            "Wrong link in on button 'Text field'"

    @pytest.mark.parametrize("key, expected", [
        ("ab123c_de-f", True),  # good
        ("a", False),  # 1 len
        ("aa", True),  # 2 len
        ("1234567890123456789012345", True),  # 25 len
        ("12345678901234567890123456", False),  # 26 len
        ("ad@3$", False),  # bad key
    ])
    def test_text_string(self, key, expected):
        self.input_page.open()
        self.input_page.input_text(key)
        assert self.input_page.check_result(key) == expected, f"Wrong text field logic for key='{key}'"

    @pytest.mark.parametrize("key, expected", [
        ("user@example.com", True),
        ("john.doe@localhost", True),
        ("user+tag@domain.com", True),
        ("u@l.com", True),
        ("plainaddress", False),
        ("@no-local-part.com", False),
        ("user@.com", False),
        ("user@localhost.", False),
        ("user@com", False),
        ("user@localhost..com", False),
    ])
    def test_email_input(self, key, expected):
        self.input_page.open()
        self.input_page.open_email_field()
        self.input_page.input_email(key)
        assert self.input_page.check_result(key) == expected, f"Wrong email field logic for key='{key}'"

    @pytest.mark.parametrize("key, expected", [
        ("Abcdef1!", True),
        ("Qwerty9@", True),
        ("Zz1#Zz1#", True),
        ("A1b2C3d4$", True),
        ("Passw0rd!", True),
        ("abcdefg1!", False),
        ("ABCDEFG1!", False),
        ("Abcdefgh!", False),
        ("Abcdefg1", False),
        ("Ab1!", False),
        ("12345678!", False),
        ("Password", False)
    ])
    def test_password_input(self, key, expected):
        self.input_page.open()
        self.input_page.open_password_field()
        self.input_page.input_password(key)
        assert self.input_page.check_result(key) == expected, f"Wrong password field logic for key='{key}'"
