from pages.products_page import ProductsPage
from pages.checkout_page import CheckOutPage
from data.product_data import product_details
from pages.cart_page import CartPage


def test_e2e_purchase_flow(login_fixture):
    # Navigate to Products Page
    product_page = ProductsPage(login_fixture)
    # Add products to the cart
    for index, product in enumerate(product_details, start=1):
        product_page.add_item_to_cart(product["locator"])
        assert product_page.verify_added_items_in_cart(
            index
        ), f"Item {index} is not added to the cart."

    # Proceed to Cart Page
    product_page.enter_cart_page()
    cart_page = CartPage(product_page.driver)
    assert cart_page.verify_cart_item_count_is_correct(len(product_details))

    # Complete Checkout
    cart_page.continue_to_complete_checkout()
    checkout_page = CheckOutPage(cart_page.driver)
    checkout_page.fill_checkout_form()
    checkout_page.verify_checkout_form_is_filled()
    checkout_page.continue_to_checkout_summary()
    assert checkout_page.verify_item_count_is_correct(len(product_details))
    assert checkout_page.verify_item_cart_list_details(product_details)
    assert checkout_page.verify_final_price()

    # Proceed and Verify Order Completion
    checkout_page.continue_to_verify_order_completion()

    # Go Back To Home Page
    checkout_page.go_back_home_page_and_verify()
