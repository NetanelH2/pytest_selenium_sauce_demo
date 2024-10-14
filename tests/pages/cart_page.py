from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    item_quantity_locator = (By.CSS_SELECTOR, 'div[data-test="item-quantity"]')
    checkout_button_locator = (By.ID, "checkout")
    checkout_form_page_url = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_count(self) -> int:
        elements = self.find_elements(*self.item_quantity_locator)
        return len(elements)

    def verify_cart_item_count_is_correct(self, expected_item_count: int) -> bool:
        actual_item_count = self.get_item_count()
        return actual_item_count == expected_item_count

    def continue_to_complete_checkout(self):
        self.find_element(*self.checkout_button_locator).click()
        assert self.is_url_opened(self.checkout_form_page_url)
