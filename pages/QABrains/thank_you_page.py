from playwright.sync_api import expect, Page


class ThankYouPage:
    def __init__(self, page: Page):
        self.page = page

        # region Validations

    def validateThankYouMessage(self, message):
        expect(
            self.page.get_by_role("heading", name="thank you for your order!")
        ).to_have_text(message)

        # endregion
