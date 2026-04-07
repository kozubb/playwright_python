from playwright.sync_api import Page, expect


class ProductListing:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.shopping_cart = page.locator('[data-test="shopping-cart-link"]')

    # region Helpers on UI elements
    # endregion

    # region Actions on UI elements
    # endregion

    # region Validations on UI elements

    # Check if shopping cart is visible on the page
    def validate_if_cart_is_visible(self):
        expect(self.shopping_cart).to_be_visible()

    # endregion
