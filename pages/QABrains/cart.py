from playwright.sync_api import expect, Page
from .helpers import Helpers


class Cart:
    def __init__(self, page: Page):
        self.page = page
        self.helpers = Helpers(self.page)

    # region Actions

    def checkout(self):
        self.page.get_by_role("button", name="checkout").click()
        self.page.wait_for_url("**/checkout-info")

    # endregion

    # region Validations

    # Validate that the product price and currency in the cart matches expected price
    def validate_product_price_and_currency_in_cart(
        self, currency_symbol, expected_price
    ):
        price_element = self.page.locator(".font-bold.text-lg.font-oswald").last
        price_text = price_element.text_content()

        # Use Helpers to validate numeric price and currency symbol
        self.helpers.price_validator(price_text, expected_price, currency_symbol)

    def validate_product_in_cart(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    # endregion
