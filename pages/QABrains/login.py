from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.login_button = page.get_by_role("button", name="login")
        self.logout_button = page.get_by_role("button", name="logout")
        self.email_input = page.get_by_role("textbox", name="email")
        self.password_input = page.get_by_role("textbox", name="password")
        self.success_message = page.get_by_role("heading", name="login successful")

    # ---------------- Actions ----------------

    def fill_email(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_password(self, password: str) -> None:
        self.password_input.fill(password)

    def press_login_button(self) -> None:
        self.login_button.click()

    def press_logout_button(self) -> None:
        self.logout_button.click()

    # ---------------- Validations ----------------

    def validate_login_success_message(self, expected_text: str) -> None:
        expect(self.success_message).to_have_text(expected_text)

    def validate_login_button_visible(self) -> None:
        expect(self.login_button).to_be_visible()

    def validate_logout_button_visible(self) -> None:
        expect(self.logout_button).to_be_visible()
