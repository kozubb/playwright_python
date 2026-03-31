from playwright.sync_api import Page


class ProductListing:
    def __init__(self, page: Page):
        self.page = page

    # region Actions

    def add_product_to_cart(self, product_name):
        products = self.page.locator(".text-lg.block")
        buttons = self.page.locator("button", has_text="add to cart")

        count = products.count()
        for i in range(count):
            name = products.nth(i).text_content()
            if name and name.strip() == product_name:
                buttons.nth(i).click()
                break

    def open_cart(self):
        basket_amount = self.page.locator(".bg-qa-clr")
        basket_amount.click()

    # endregion
