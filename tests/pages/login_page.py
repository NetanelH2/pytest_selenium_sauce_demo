from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://www.saucedemo.com"
    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    product_page_title_text = "Products"

    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_url(self.url)
        self.is_url_opened(self.url)

    def login_user(self, username: str, password: str):
        self.find_element(*self.username_locator).send_keys(username)
        self.find_element(*self.password_locator).send_keys(password)
        self.find_element(*self.login_button_locator).click()

    def verify_successful_login(self) -> bool:
        return self.is_text_present(self.product_page_title_text)

    def verify_error_login_message(self, text: str) -> bool:
        return self.is_text_present(text)
