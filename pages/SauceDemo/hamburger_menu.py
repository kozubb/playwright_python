from playwright.sync_api import Page, expect


class HamburgerMenu:
    def __init__(self, page: Page):
        self.page = page

    # region Actions on UI elements

    # Press at hamburger menu icon
    def press_hamburger_menu_icon(self):
        self.page.get_by_role("button", name="open menu").click()

    # Press at hamburger menu icon
    def press_hamburger_menu_logout_button(self):
        self.page.get_by_role("link", name="logout").click()

    # endregion

    # region Validations on UI elements

    # endregion
