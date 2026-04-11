from playwright.sync_api import Page, expect


class ThankYouPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.thank_you_text = self.page.locator('[data-test="complete-header"]')
        self.back_home_button = self.page.locator('[data-test="back-to-products"]')

    # region Actions

    # Click "Back Home" button
    def pressBackHomeButton(self):
        self.back_home_button.click()

    # endregion

    # region Validations

    # Validate "Thank You" page message text
    def validate_thank_you_text(self, expected_text):
        expect(self.thank_you_text).to_have_text(expected_text)

    # endregion
