from playwright.sync_api import Page, expect


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.name_input = page.get_by_role("textbox", name="name")
        self.country_select = page.get_by_role("combobox", name="select country")
        self.account_type_select = page.get_by_role("combobox", name="account type")
        self.email_input = page.get_by_role("textbox", name="email")
        self.password_input = page.get_by_role("textbox", name="password").first
        self.confirm_password_input = page.get_by_role(
            "textbox", name="confirm password"
        )
        self.signup_button = page.get_by_role("button", name="signup")
        self.success_message = page.get_by_role(
            "heading", name="registration successful"
        )

    # region Actions

    def open_register_page(self, endpoint):
        self.page.goto(f"{endpoint}registration")

    def fill_register_form(self, data):
        self.name_input.fill(data["name"])
        self.country_select.select_option(data["country"])
        self.account_type_select.select_option(data["accountType"])
        self.email_input.fill(data["email"])
        self.password_input.fill(data["password"])
        self.confirm_password_input.fill(data["password"])

    def submit_form(self):
        self.signup_button.click()

    # end region

    # region Validations

    def validate_registration_success(self, expected_text):
        expect(self.success_message).to_have_text(expected_text)

    # end region
