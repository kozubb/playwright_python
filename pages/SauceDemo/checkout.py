from playwright.sync_api import Page


class Checkout:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.continue_button = self.page.get_by_role("button", name="continue")

    # region Actions on UI elements

    # Fill checkout input by input name and expected text
    def fill_checkout_input(self, input_name, expected_text):
        self.page.get_by_role("textbox", name=input_name).fill(expected_text)

    # Press continue button
    def press_continue_button(self):
        self.continue_button.click()

    # endregion

    # region Validations on UI elements

    # endregion
