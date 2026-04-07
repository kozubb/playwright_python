from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.login_button = page.get_by_role("button", name="login")
        self.error_message = page.locator('[data-test="error"]')

    # region Actions on UI elements

    # Fill input field by input name and expected text
    def fill_input(self, input_name, expected_text):
        self.page.get_by_role("textbox", name=input_name).fill(expected_text)

    # Press login button
    def press_login_button(self):
        self.login_button.click()

    # endregion

    # region Validations on UI elements

    # Check if login button is visible on the page
    def validate_if_login_button_is_visible(self):
        expect(self.login_button).to_be_visible()

    # Check login error message
    def validate_login_error_message(self, expected_text):
        expect(self.error_message).to_contain_text(expected_text)

    # Check visibility of login error message
    def validate_if_login_error_message_is_visible(self, visible=True):
        if visible:
            expect(self.error_message).to_be_visible()
        else:
            expect(self.error_message).to_be_hidden()

    # endregion
