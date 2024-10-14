from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.person_data import generate_person_details


class CheckOutPage(BasePage):
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

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_count(self) -> int:
        elements = self.find_elements(*self.item_quantity_locator)
        return len(elements)

    def verify_item_count_is_correct(self, expected_item_count: int) -> bool:
        actual_item_count = self.get_item_count()
        return actual_item_count == expected_item_count

    def fill_checkout_form(self):
        self.first_name, self.last_name, self.postal_code = generate_person_details()
        self.find_element(*self.checkout_form_first_name_locator).send_keys(
            self.first_name
        )
        self.find_element(*self.checkout_form_last_name_locator).send_keys(
            self.last_name
        )
        self.find_element(*self.checkout_form_postal_code_locator).send_keys(
            self.postal_code
        )

    def verify_checkout_form_is_filled(self) -> bool:
        return all(
            self.is_text_present(text)
            for text in (self.first_name, self.last_name, self.postal_code)
        )

    def continue_to_checkout_summary(self):
        self.find_element(*self.checkout_continue_button_locator).click()
        assert self.is_url_opened(self.checkout_summary_url)

    def verify_item_cart_list_details(self, items: list[dict[str, str]]):
        return all(
            self.is_text_present(text)
            for item in items
            for key, text in item.items()
            if key != "locator"
        )

    def __calculate_total_price_before_tax(self) -> float:
        price_list_locators = self.find_elements(
            *self.checkout_summary_item_price_locator
        )
        prices: list[float] = [
            float(price.text.replace("$", "")) for price in price_list_locators
        ]
        return sum(prices)

    def __calculate_tax_price(self) -> float:
        return round((self.__calculate_total_price_before_tax() * 0.08), 2)

    def verify_final_price(self) -> bool:
        total_price = (
            self.__calculate_total_price_before_tax() + self.__calculate_tax_price()
        )
        return self.is_text_present(str(total_price))

    def continue_to_verify_order_completion(self):
        self.find_element(*self.checkout_summary_finish_button_locator).click()
        assert self.is_text_present("Thank you for your order!")
        assert self.is_url_opened(self.finish_order_url)

    def go_back_home_page_and_verify(self):
        self.find_element(*self.go_back_home_page_button_locator).click()
        assert self.is_url_opened(self.home_page_url)
