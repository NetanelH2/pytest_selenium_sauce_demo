from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    item_quantity_locator = (By.CSS_SELECTOR, 'div[data-test="item-quantity"]')
    checkout_form_first_name_locator = (By.ID, "first-name")
    checkout_form_last_name_locator = (By.ID, "last-name")
    checkout_form_postal_code_locator = (By.ID, "postal-code")
    checkout_continue_button_locator = (By.ID, "continue")
    checkout_summary_url = "https://www.saucedemo.com/checkout-step-two.html"
    checkout_summary_item_price_locator = (
        By.CSS_SELECTOR,
        'div[data-test="inventory-item-price"]',
    )
    checkout_summary_total_price_before_tax_locator = (
        By.CSS_SELECTOR,
        'div[data-test="tax-label"]',
    )
    checkout_summary_finish_button_locator = (By.ID, "finish")
    finish_order_url = "https://www.saucedemo.com/checkout-complete.html"
    go_back_home_page_button_locator = (By.ID, "back-to-products")
    home_page_url = "https://www.saucedemo.com/inventory.html"