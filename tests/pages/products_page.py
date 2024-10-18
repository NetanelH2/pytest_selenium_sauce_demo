from pages.base_page import BasePage
from locators.products_page_locators import ProductsPageLocators


class ProductsPage(BasePage):
    products_page = ProductsPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self, item__locator: str):
        locator = self.products_page.get_add_to_cart_button_locator(item__locator)
        self.find_element(*locator).click()

    def get_cart_count_locator_number(self) -> int:
        locator = self.find_element(*self.products_page.cart_count_locator)
        return int(locator.text)

    def verify_added_items_in_cart(self, expected_count: int) -> bool:
        actual_cart_count = self.get_cart_count_locator_number()
        return actual_cart_count == expected_count

    def enter_cart_page(self):
        self.find_element(*self.products_page.cart_icon_locator).click()
        assert self.is_url_opened("https://www.saucedemo.com/cart.html")
