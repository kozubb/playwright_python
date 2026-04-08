from pages.QABrains.cart import Cart
from pages.QABrains.checkout import Checkout
from pages.QABrains.helpers import Helpers
from pages.QABrains.overview import Overview
from pages.QABrains.product_listing import ProductListing
from pages.QABrains.thank_you_page import ThankYouPage
from test_data.QABrains.test_data import test_data


def test_e2e_place_order(page):
    cart = Cart(page)
    checkout = Checkout(page)
    helpers = Helpers(page)
    overview = Overview(page)
    product_listing = ProductListing(page)
    thank_you_page = ThankYouPage(page)

    # Step 1: Login
    helpers.login_as(
        f'{test_data["Endpoint"]}/ecommerce/login',
        test_data["Users"]["OrderUser"]["Username"],
        test_data["Users"]["OrderUser"]["Password"],
    )

    # Step 2:  Add product to cart
    product_listing.add_product_to_cart(test_data["Products"]["Shoe"]["Name"])
    product_listing.open_cart()

    # Step 3:  Verify cart
    cart.validate_product_in_cart(test_data["Products"]["Shoe"]["Name"])
    cart.validate_product_price_and_currency_in_cart(
        test_data["CurrencySymbol"], test_data["Products"]["Shoe"]["Price"]
    )
    cart.checkout()

    # Step 4:  Fill checkout form
    checkout.fill_first_name(test_data["Users"]["OrderUser"]["FirstName"])
    checkout.fill_last_name(test_data["Users"]["OrderUser"]["LastName"])
    checkout.validate_zip_code(test_data["Users"]["OrderUser"]["Zipcode"])
    checkout.press_continue_button()

    # Step 5:  Review and finish order
    overview.validate_total_price_and_currency_in_overview(
        test_data["CurrencySymbol"],
        test_data["Products"]["Shoe"]["Price"] + test_data["DeliveryPrice"],
    )
    overview.finish_order()

    # Step 6:  Verify Thank You page
    thank_you_page.validateThankYouMessage(test_data["Messages"]["ThankYouMessage"])
