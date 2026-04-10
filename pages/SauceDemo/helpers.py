from .login import LoginPage
from playwright.sync_api import Page
import re


class Helpers:
    def __init__(self, page: Page):
        self.page = page

    # Login into SauceDemo with given credentials
    def login_as(self, endpoint, username, password):

        login_page = LoginPage(self.page)

        # Visit the login page
        self.page.goto(endpoint)

        # Fill in username and password, then submit
        login_page.fill_input("username", username)
        login_page.fill_input("password", password)
        login_page.press_login_button()

        return self

    # Remove currency symbols from a string and return numeric part
    def remove_currency_symbol(text):
        return re.sub(r"[\$£€+]", "", text).strip()

    # Remove numeric price and return only currency symbols
    def remove_price(text):
        return re.sub(r"[0-9]+,?.[0-9]{2}", "", text).strip()

    # Remove special characters and convert string to lowercase
    def remove_special_chars(text):
        return re.sub(r'[&/\\#,+()~%_.\'":*?<>{} ]', "", text).lower()

    # Remove letters, colons, and spaces from a string
    def remove_letters_colon_and_space(text):
        return re.sub(r"[a-zA-Z:\s]", "", text)

    # Convert comma to dot and parse string to float
    def change_comma_sign(text):
        return float(text.strip().replace(",", "."))

    # Validate that price and currency symbol match expected values
    def price_validator(
        self, current_price_element, expected_price_value, expected_currency_symbol
    ):
        expected_price_as_number_fixed = float(f"{expected_price_value:.2f}")
        price_without_letters = self.remove_letters_colon_and_space(
            current_price_element
        )
        price = self.change_comma_sign(
            self.remove_currency_symbol(price_without_letters)
        )
        currency_symbol_without_letters = self.remove_letters_colon_and_space(
            current_price_element
        )
        currency_symbol = self.remove_special_chars(
            self.removePrice(currency_symbol_without_letters)
        )

        # Assert that numeric price matches expected
        assert round(price, 2) == round(expected_price_as_number_fixed, 2)

        # Assert that currency symbol matches expected
        assert currency_symbol == expected_currency_symbol

        return self
