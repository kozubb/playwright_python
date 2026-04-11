from playwright.sync_api import Page, expect
from .helpers import Helpers


class Overview:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.payment_method = page.locator('[data-test="payment-info-value"]')
        self.delivery_method = page.locator('[data-test="shipping-info-value"]')
        self.subtotal_price = page.locator('[data-test="subtotal-label"]')
        self.tax_price = page.locator('[data-test="tax-label"]')
        self.total_price = page.locator('[data-test="total-label"]')
        self.finish_button = page.locator('[data-test="finish"]')

    # region Actions on UI elements

    # Press finish button
    def press_finish_button(self):
        self.finish_button.click()

    # endregion

    # region Validations on UI elements

    # Check payment method
    def validate_payment_method(self, expected_text):
        expect(self.payment_method).to_have_text(expected_text)

    # Check delivery method
    def validate_delivery_method(self, expected_text):
        expect(self.delivery_method).to_have_text(expected_text)

    # Validate subtotal price (currency + numeric value)
    def validate_subtotal(self, expected_price, currency, page):
        helpers = Helpers(page)
        subtotal_price_text = self.subtotal_price.text_content()
        helpers.price(subtotal_price_text, expected_price, currency)
        return self

    # Validate total price, check currency
    def validate_total_price(self, expected_price, currencySymbol, page):
        helpers = Helpers(page)
        total_price_text = self.total_price.textContent()

        helpers.price_validator(total_price_text, expected_price, currencySymbol)
        return self

    # endregion
