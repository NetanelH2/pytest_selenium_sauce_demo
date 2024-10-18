from selenium.webdriver.common.by import By


class ProductsPageLocators:
    cart_count_locator = (By.CSS_SELECTOR, 'span[data-test="shopping-cart-badge"]')
    cart_icon_locator = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def get_add_to_cart_button_locator(self, item_name):
        return (By.CSS_SELECTOR, f'button[data-test="add-to-cart-{item_name}"]')
