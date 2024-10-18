from selenium.webdriver.common.by import By


class CartPageLocators:
    item_quantity_locator = (By.CSS_SELECTOR, 'div[data-test="item-quantity"]')
    checkout_button_locator = (By.ID, "checkout")
    checkout_form_page_url = "https://www.saucedemo.com/checkout-step-one.html"
