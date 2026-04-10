from .helpers import Helpers
from playwright.sync_api import Page, expect


class ProductDetails:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.remove_button = page.locator('[data-test="remove"]')
        self.back_button = page.locator('[data-test="back-to-products"]')
        self.product_title = page.locator('[data-test="inventory-item-name"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')

    # region Actions

    # Click "Add to Cart" button
    def press_add_to_cart_button(self):
        self.add_to_cart_button.click()

    # Click "Remove" button
    def press_remove_button(self):
        self.remove_button.click()

    # Click "Back to Products" button
    def press_back_button(self):
        self.back_button.click()

    # endregion

    # region Validations

    # Validate product title text
    def validate_product_title(self, expected_title):
        expect(self.product_title).to_have_text(expected_title)

    # Validate product price text (numeric + currency)
    def validate_product_price(self, expected_price, currency_symbol, page):
        helpers = Helpers(page)

        price_text = self.product_price.text_content()
        # Use Helpers to validate numeric price and currency symbol
        helpers.price_validator(price_text, expected_price, currency_symbol)

    # Validate if "Remove" button is visible
    def validate_if_remove_buttonIsVisible(self):
        expect(self.remove_button).to_be_visible()

    # endregion
