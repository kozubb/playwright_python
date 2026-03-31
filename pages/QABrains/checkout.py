from playwright.sync_api import expect, Page


class Checkout:
    def __init__(self, page: Page):
        self.page = page

    # region Actions

    # Fill first name field
    def fill_first_name(self, first_name):
        self.page.get_by_role("textbox", name="ex. john").fill(first_name)

    # Fill last name field
    def fill_last_name(self, last_name):
        self.page.get_by_role("textbox", name="ex. doe").fill(last_name)

    # Click continue button
    def press_continue_button(self):
        self.page.get_by_role("button", name="continue").click()

    # endregion

    # region Validations

    # Validate zip code field value
    def validate_zip_code(self, zip_code):
        locator = self.page.locator(f'.form-control[value="{zip_code}"]')
        expect(locator).to_have_value(str(zip_code))

    # endregion
