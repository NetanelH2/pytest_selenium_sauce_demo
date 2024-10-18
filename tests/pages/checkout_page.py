from pages.base_page import BasePage
from data.person_data import generate_person_details
from locators.checkout_page_locators import CheckoutPageLocators


class CheckOutPage(BasePage):
    checkout_page = CheckoutPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_count(self) -> int:
        elements = self.find_elements(*self.checkout_page.item_quantity_locator)
        return len(elements)

    def verify_item_count_is_correct(self, expected_item_count: int) -> bool:
        actual_item_count = self.get_item_count()
        return actual_item_count == expected_item_count

    def fill_checkout_form(self):
        self.first_name, self.last_name, self.postal_code = generate_person_details()
        self.find_element(
            *self.checkout_page.checkout_form_first_name_locator
        ).send_keys(self.first_name)
        self.find_element(
            *self.checkout_page.checkout_form_last_name_locator
        ).send_keys(self.last_name)
        self.find_element(
            *self.checkout_page.checkout_form_postal_code_locator
        ).send_keys(self.postal_code)

    def verify_checkout_form_is_filled(self) -> bool:
        return all(
            self.is_text_present(text)
            for text in (self.first_name, self.last_name, self.postal_code)
        )

    def continue_to_checkout_summary(self):
        self.find_element(*self.checkout_page.checkout_continue_button_locator).click()
        assert self.is_url_opened(self.checkout_page.checkout_summary_url)

    def verify_item_cart_list_details(self, items: list[dict[str, str]]):
        return all(
            self.is_text_present(text)
            for item in items
            for key, text in item.items()
            if key != "locator"
        )

    def __calculate_total_price_before_tax(self) -> float:
        price_list_locators = self.find_elements(
            *self.checkout_page.checkout_summary_item_price_locator
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
        self.find_element(
            *self.checkout_page.checkout_summary_finish_button_locator
        ).click()
        assert self.is_text_present("Thank you for your order!")
        assert self.is_url_opened(self.checkout_page.finish_order_url)

    def go_back_home_page_and_verify(self):
        self.find_element(*self.checkout_page.go_back_home_page_button_locator).click()
        assert self.is_url_opened(self.checkout_page.home_page_url)
