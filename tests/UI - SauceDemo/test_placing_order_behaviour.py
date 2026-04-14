from pages.SauceDemo.cart import Cart
from pages.SauceDemo.checkout import Checkout
from pages.SauceDemo.helpers import Helpers
from pages.SauceDemo.overview import Overview
from pages.SauceDemo.product_listing import ProductListing
from pages.SauceDemo.thank_you_page import ThankYouPage
from test_data.SauceDemo.test_data import test_data


# E2E test: Place an order from product listing to Thank You page
def test_place_order(page):
    # Step 1: Initialize all page objects
    productListing = ProductListing(page)
    cart = Cart(page)
    helpers = Helpers(page)
    checkout = Checkout(page)
    overview = Overview(page)
    thankYou = ThankYouPage(page)

    # Step 2: Log in as standard user
    helpers.login_as(
        test_data["Endpoint"],
        test_data["Users"]["StandardUser"]["Username"],
        test_data["Users"]["StandardUser"]["Password"],
    )
    # Step 3: Verify inventory page is loaded and shopping cart icon is visible
    page.wait_for_url(f'{test_data["Endpoint"]}/inventory.html')
    productListing.validate_if_cart_is_visible()

    # Step 4: Add products from listing page to cart
    productListing.press_add_to_order_button(test_data["Products"]["Backpack"]["Name"])
    productListing.validate_shopping_cart_amount("1")  # Validate 1 item in cart

    productListing.press_add_to_order_button(test_data["Products"]["BikeLight"]["Name"])
    productListing.validate_shopping_cart_amount("2")  # Validate 2 items in cart

    # Step 5: Open cart and validate product details
    productListing.press_shopping_cart_icon()

    # Validate product titles
    cart.validate_product_title_in_basket(
        test_data["Products"]["Backpack"]["Id"],
        test_data["Products"]["Backpack"]["Name"],
    )
    cart.validate_product_title_in_basket(
        test_data["Products"]["BikeLight"]["Id"],
        test_data["Products"]["BikeLight"]["Name"],
    )

    # Validate product quantities
    cart.validate_product_quantity_in_cart(0, "1")
    cart.validate_product_quantity_in_cart(1, "1")

    # Validate product prices and currency
    cart.validate_product_price_and_currency_in_cart(
        0, test_data["CurrencySymbol"], test_data["Products"]["Backpack"]["Price"], page
    )
    cart.validate_product_price_and_currency_in_cart(
        1,
        test_data["CurrencySymbol"],
        test_data["Products"]["BikeLight"]["Price"],
        page,
    )

    # Step 6: Proceed to checkout
    cart.press_checkout_button()

    # Step 7: Fill in checkout information
    checkout.fill_checkout_input(
        test_data["CheckoutForm"]["FirstNameText"],
        test_data["Users"]["OrderUser"]["FirstName"],
    )
    checkout.fill_checkout_input(
        test_data["CheckoutForm"]["LastNameText"],
        test_data["Users"]["OrderUser"]["LastName"],
    )
    checkout.fill_checkout_input(
        test_data["CheckoutForm"]["ZipcodeText"],
        test_data["Users"]["OrderUser"]["Zipcode"],
    )
    checkout.press_continue_button()

    # Step 8: Validate overview page details
    overview.validate_payment_method(test_data["PaymentMethod"])  # Payment method
    overview.validate_delivery_method(test_data["DeliveryMethod"])  # Shipping method
    overview.validate_subtotal(
        test_data["Products"]["Backpack"]["Price"]
        + test_data["Products"]["BikeLight"]["Price"],
        test_data["CurrencySymbol"],
        page,
    )  # Subtotal
    overview.validate_total_price(
        (
            test_data["Products"]["Backpack"]["Price"]
            + test_data["Products"]["BikeLight"]["Price"]
        )
        * test_data["Tax"]
        + test_data["Products"]["Backpack"]["Price"]
        + test_data["Products"]["BikeLight"]["Price"],
        test_data["CurrencySymbol"],
        page,
    )  # Total price

    # Step 9: Finish the order
    overview.press_finish_button()

    # Step 10: Validate Thank You page message
    thankYou.validate_thank_you_text(test_data["Messages"]["ThankYouMessage"])
