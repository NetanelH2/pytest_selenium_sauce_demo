from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    cart_page = CartPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_count(self) -> int:
        elements = self.find_elements(*self.cart_page.item_quantity_locator)
        return len(elements)

    def verify_cart_item_count_is_correct(self, expected_item_count: int) -> bool:
        actual_item_count = self.get_item_count()
        return actual_item_count == expected_item_count

    def continue_to_complete_checkout(self):
        self.find_element(*self.cart_page.checkout_button_locator).click()
        assert self.is_url_opened(self.cart_page.checkout_form_page_url)
