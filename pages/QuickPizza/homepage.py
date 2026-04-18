from playwright.sync_api import Page, expect


class Homepage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.pizza_button = self.page.get_by_role("button", name="pizza, please!")
        self.recommend_button = self.page.get_by_role("button", name="love it!")
        self.no_thanks_button = self.page.get_by_role("button", name="no thanks")
        self.rating_message = self.page.locator("#rate-result")

    # region Actions on UI elements

    # Press pizza button
    def press_pizza_button(self):
        self.pizza_button.click()

    # Press 'love it' button
    def press_recommend_rutton(self):
        self.recommend_button.click()

    # Press 'no thanks' button
    def press_no_thanks_button(self):
        self.no_thanks_button.click()

    # endregion

    # region Validations on UI elements

    # Check if 'no thanks' button is visible on the page
    def validate_if_no_thanks_is_visible(self):
        expect(self.no_thanks_button).to_be_visible()

    # Check message after rating
    def validate_rating_message(self, expected_text):
        expect(self.rating_message).to_have_text(expected_text)

    # #endregion
