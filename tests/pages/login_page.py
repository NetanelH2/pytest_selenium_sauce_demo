from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    login_page = LoginPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(self.login_page.url)
        self.is_url_opened(self.login_page.url)

    def login_user(self, username: str, password: str):
        self.find_element(*self.login_page.username_locator).send_keys(username)
        self.find_element(*self.login_page.password_locator).send_keys(password)
        self.find_element(*self.login_page.login_button_locator).click()

    def verify_successful_login(self) -> bool:
        return self.is_text_present(self.login_page.product_page_title_text)

    def verify_error_login_message(self, text: str) -> bool:
        return self.is_text_present(text)
