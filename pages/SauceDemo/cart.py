from playwright.sync_api import Page, expect
from .helpers import Helpers


class Cart:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.item_quantity = page.locator('[data-test="item-quantity"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.helpers = Helpers(page)

    # region Helpers on UI elements

    # Return locator for product title in cart
    def product_title_cart(self, product_id):
        return self.page.locator(f'[data-test="item-{product_id}-title-link"]')

    # Return locator for remove product button in cart
    def remove_product_button_cart(self, product_name):
        return self.page.locator(f'[data-test="remove-{product_name}"]')

    # endregion

    # region Actions on UI elements

    # Press checkout button
    def press_checkout_button(self):
        self.checkout_button.click()

    # Click product title in cart
    def press_product_title(self, product_id):
        self.product_title_cart(product_id).click()

    # Press remove product button in cart
    def press_remove_product_button_cart(self, product_name):
        self.remove_product_button_cart(product_name).click()

    # Press continue shopping button
    def press_continue_shopping_button(self):
        self.continue_shopping_button.click()

    # endregion

    # region Validations on UI elements

    # Validate product quantity by position
    def validate_product_quantity_in_cart(self, position, quantity):
        expect(self.item_quantity.nth(position)).to_have_text(quantity)

    # Validate product title by product id
    def validate_product_title_in_basket(self, product_id, product_title):
        expect(self.product_title_cart(product_id)).to_have_text(product_title)

    # Validate product price in cart by position, validating currency and numeric value
    def validate_product_price_and_currency_in_cart(
        self, position, currency_symbol, expected_price, page
    ):
        helpers = Helpers(page)
        price_element = self.product_price.nth(position)
        price_text = price_element.text_content()

        # Use Helpers to validate numeric price and currency symbol
        helpers.price_validator(price_text, expected_price, currency_symbol)


# endregion
