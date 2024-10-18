from selenium.webdriver.common.by import By


class LoginPageLocators:
    url = "https://www.saucedemo.com"
    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
    product_page_title_text = "Products"
