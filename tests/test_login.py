import pytest
from pages.login_page import LoginPage
from data.user_data import user_data


@pytest.mark.parametrize("username, password, expected_error_message", user_data)
def test_login(driver, username, password, expected_error_message):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user(username, password)
    if expected_error_message == "":
        assert login_page.verify_successful_login(), "Login failed."
    else:
        assert login_page.verify_error_login_message(
            expected_error_message
        ), "Error message is not displayed."
