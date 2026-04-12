from playwright.sync_api import Page
from pages.SauceDemo.helpers import Helpers
from pages.SauceDemo.cart import Cart
from pages.SauceDemo.product_details import ProductDetails
from pages.SauceDemo.product_listing import ProductListing
from test_data.SauceDemo.test_data import test_data


# E2E test: Add products from listing page and verify cart content
def test_add_products_to_cart_verify(page):
    # Step 1: Initialize page objects
    product_listing = ProductListing(page)
    cart = Cart(page)
    helpers = Helpers(page)

    # Step 2: Log in as standard user
    helpers.login_as(
        test_data["Endpoint"],
        test_data["Users"]["StandardUser"]["Username"],
        test_data["Users"]["StandardUser"]["Password"],
    )

    # Step 3: Verify inventory page is loaded
    page.wait_for_url(f'{test_data["Endpoint"]}/inventory.html')
    product_listing.validate_if_cart_is_visible()

    # Step 4: Add products from listing page
    product_listing.press_add_to_order_button(test_data["Products"]["Backpack"]["Name"])
    product_listing.validate_shopping_cart_amount("1")

    product_listing.press_add_to_order_button(
        test_data["Products"]["BikeLight"]["Name"]
    )
    product_listing.validate_shopping_cart_amount("2")

    # Step 5: Open cart and validate product details
    product_listing.press_shopping_cart_icon()

    cart.validate_product_title_in_basket(
        test_data["Products"]["Backpack"]["Id"],
        test_data["Products"]["Backpack"]["Name"],
    )
    cart.validate_product_title_in_basket(
        test_data["Products"]["BikeLight"]["Id"],
        test_data["Products"]["BikeLight"]["Name"],
    )

    cart.validate_product_quantity_in_cart(0, "1")
    cart.validate_product_quantity_in_cart(1, "1")

    cart.validate_product_price_and_currency_in_cart(
        0, test_data["CurrencySymbol"], test_data["Products"]["Backpack"]["Price"], page
    )
    cart.validate_product_price_and_currency_in_cart(
        1,
        test_data["CurrencySymbol"],
        test_data["Products"]["BikeLight"]["Price"],
        page,
    )


# E2E test: Add products from PDP and verify cart content
def test_add_products_from_pdp_verify_cart(page):
    # Step 1: Initialize page objects
    product_listing = ProductListing(page)
    cart = Cart(page)
    product_details = ProductDetails(page)
    helpers = Helpers(page)

    # Step 2: Log in as standard user
    helpers.login_as(
        test_data["Endpoint"],
        test_data["Users"]["StandardUser"]["Username"],
        test_data["Users"]["StandardUser"]["Password"],
    )

    # Step 3: Verify inventory page is loaded
    page.wait_for_url(f'{test_data["Endpoint"]}/inventory.html')
    product_listing.validate_if_cart_is_visible()

    # Step 4: Add productBackpack from PDP
    product_listing.press_product_image(test_data["Products"]["Backpack"]["Name"])
    page.wait_for_url(
        f'{test_data["Endpoint"]}/inventory-item.html?id={test_data["Products"]["Backpack"]["Id"]}'
    )
    product_details.validate_product_title(test_data["Products"]["Backpack"]["Name"])
    product_details.validate_product_price(
        test_data["Products"]["Backpack"]["Price"], test_data["CurrencySymbol"], page
    )
    product_details.press_add_to_cart_button()
    product_listing.validate_shopping_cart_amount("1")
    product_details.press_back_button()

    # Step 5: Add productBikeLight from PDP
    product_listing.press_product_image(test_data["Products"]["BikeLight"]["Name"])
    page.wait_for_url(
        f'{test_data["Endpoint"]}/inventory-item.html?id={test_data["Products"]["BikeLight"]["Id"]}'
    )
    product_details.validate_product_title(test_data["Products"]["BikeLight"]["Name"])
    product_details.validate_product_price(
        test_data["Products"]["BikeLight"]["Price"], test_data["CurrencySymbol"], page
    )
    product_details.press_add_to_cart_button()
    product_listing.validate_shopping_cart_amount("2")

    # Step 6: Open cart and validate product details
    product_listing.press_shopping_cart_icon()

    cart.validate_product_title_in_basket(
        test_data["Products"]["Backpack"]["Id"],
        test_data["Products"]["Backpack"]["Name"],
    )
    cart.validate_product_title_in_basket(
        test_data["Products"]["BikeLight"]["Id"],
        test_data["Products"]["BikeLight"]["Name"],
    )

    cart.validate_product_quantity_in_cart(0, "1")
    cart.validate_product_quantity_in_cart(1, "1")

    cart.validate_product_price_and_currency_in_cart(
        0, test_data["CurrencySymbol"], test_data["Products"]["Backpack"]["Price"], page
    )
    cart.validate_product_price_and_currency_in_cart(
        1,
        test_data["CurrencySymbol"],
        test_data["Products"]["BikeLight"]["Price"],
        page,
    )


# E2E test: Prevent duplicate adding of same product
def test_add_products_from_pdp_verify_duplicate_add_not_possible(page):
    product_listing = ProductListing(page)
    product_details = ProductDetails(page)
    helpers = Helpers(page)

    # Step 2: Log in as standard user
    helpers.login_as(
        test_data["Endpoint"],
        test_data["Users"]["StandardUser"]["Username"],
        test_data["Users"]["StandardUser"]["Password"],
    )

    # Step 3: Verify inventory page is loaded
    page.wait_for_url(f'{test_data["Endpoint"]}/inventory.html')
    product_listing.validate_if_cart_is_visible()

    # Step 4: Add productBackpack from PDP
    product_listing.press_product_image(test_data["Products"]["Backpack"]["Name"])
    page.wait_for_url(
        f'{test_data["Endpoint"]}/inventory-item.html?id={test_data["Products"]["Backpack"]["Id"]}'
    )
    product_details.validate_product_title(test_data["Products"]["Backpack"]["Name"])
    product_details.validate_product_price(
        test_data["Products"]["Backpack"]["Price"], test_data["CurrencySymbol"], page
    )
    product_details.press_add_to_cart_button()
    product_listing.validate_shopping_cart_amount("1")
    product_details.validate_if_remove_button_is_visible()
    product_details.press_back_button()

    # Step 5: Verify "Add to Cart" button is disabled for productBackpack
    product_listing.validate_if_remove_button_is_visible(
        test_data["Products"]["Backpack"]["Name"]
    )

    # Step 6: Add productBikeLight from PLP
    product_listing.press_add_to_order_button(
        test_data["Products"]["BikeLight"]["Name"]
    )
    product_listing.validate_shopping_cart_amount("2")
    product_listing.validate_if_remove_button_is_visible(
        test_data["Products"]["BikeLight"]["Name"]
    )

    # Step 7: Verify "Add to Cart" button is disabled for productBikeLight
    product_listing.validate_if_remove_button_is_visible(
        test_data["Products"]["BikeLight"]["Name"]
    )
