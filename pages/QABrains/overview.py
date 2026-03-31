from playwright.sync_api import Page
from .helpers import Helpers


class Overview:
    def __init__(self, page: Page):
        self.page = page
        self.helpers = Helpers(page)

    # region Validations

    # Validate that the total price and currency in the overview matches expected price
    def validate_total_price_and_currency_in_overview(
        self, currency_symbol, expected_price
    ):
        price_element = self.page.locator("p.text-md").last
        price_text = price_element.text_content()

        if not price_text:
            raise Exception("Price not found")

        # Use Helpers to validate numeric price and currency symbol
        self.helpers.price_validator(price_text, expected_price, currency_symbol)

    # endregion

    # region Actions

    def finish_order(self):
        self.page.get_by_role("button", name="finish").click()
        self.page.wait_for_url("**/checkout-complete**")

    # endregion
