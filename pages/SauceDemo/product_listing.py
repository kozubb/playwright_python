from playwright.sync_api import Page, expect
import re


class ProductListing:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')
        self.shopping_cart_amount = page.locator('[data-test="shopping-cart-badge"]')

    # region Helpers on UI elements
    def format_product_name(self, product_name):
        return re.sub(r"\s+", "-", product_name.lower())

    # Return locator for add to order button
    def add_to_order_button(self, product_name):
        formatted_name = self.format_product_name(product_name)
        return self.page.locator(f'[data-test="add-to-cart-{formatted_name}"]')

    # Return locator for remove product button
    def remove_product_button(self, product_name):
        formatted_name = self.format_product_name(product_name)
        return self.page.locator(f'[data-test="remove-{formatted_name}"]')

    # Return locator for product image for opening pdp
    def product_image(self, product_name):
        formatted_name = self.format_product_name(product_name)
        return self.page.locator(f'[data-test="inventory-item-{formatted_name}-img"]')

    # endregion

    # region Actions on UI elements

    # Press add to order button for specific product
    def press_add_to_order_button(self, product_name):
        self.add_to_order_button(product_name).click()

    # Press remove product button for specific product
    def press_remove_product_button(self, product_name):
        self.remove_product_button(product_name).click()

    # Press product image for specific product
    def press_product_image(self, product_name):
        self.product_image(product_name).click()

    # Press shopping cart icon
    def press_shopping_cart_icon(self):
        self.shopping_cart.click()

    # endregion

    # region Validations on UI elements

    # Check if shopping cart is visible on the page
    def validate_if_cart_is_visible(self):
        expect(self.shopping_cart).to_be_visible()

    # Check if remove button is visible for specific product
    def validate_if_remove_button_is_visible(self, product_name):
        expect(self.remove_product_button(product_name)).to_be_visible()

    # Check shopping cart amount
    def validateShoppingCartAmount(self, expected_number):
        expect(self.shopping_cart_amount).to_have_text(expected_number)

    # endregion
