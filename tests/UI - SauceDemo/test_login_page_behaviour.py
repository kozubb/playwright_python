from pages.SauceDemo.login import LoginPage
from pages.SauceDemo.hamburger_menu import HamburgerMenu
from pages.SauceDemo.product_listing import ProductListing
from test_data.SauceDemo.test_data import test_data


# E2E test: Successful login and logout
def test_login_and_logout_success(page):
    # Step 1: Initialize page objects
    login = LoginPage(page)
    product_listing = ProductListing(page)
    hamburger_menu = HamburgerMenu(page)

    # Step 2: Navigate to the login page
    page.goto(test_data["Endpoint"])

    # Step 3: Fill in the login form with valid credentials
    login.fill_input("username", test_data["Users"]["StandardUser"]["Username"])
    login.fill_input("password", test_data["Users"]["StandardUser"]["Password"])

    # Step 4: Press the login button
    login.press_login_button()

    # Step 5: Verify that inventory page is loaded and cart is visible
    page.wait_for_url(f'{test_data["Endpoint"]}/inventory.html')
    product_listing.validate_if_cart_is_visible()

    # Step 6: Open hamburger menu and log out
    hamburger_menu.press_hamburger_menu_icon()
    hamburger_menu.press_hamburger_menu_logout_button()

    # Step 7: Verify return to login page
    page.wait_for_url(f'{test_data["Endpoint"]}')
    login.validate_if_login_button_is_visible()


# E2E test: Login with wrong password
def test_login_wrong_password(page):
    # Step 1: Initialize page objects
    login = LoginPage(page)
    # Step 2: Navigate to the login page

    page.goto(test_data["Endpoint"])

    # Step 3: Fill in the login form with username and incorrect password
    login.fill_input("username", test_data["Users"]["StandardUser"]["Username"])
    login.fill_input(
        "password", test_data["Users"]["StandardUser"]["IncorrectPassword"]
    )

    # Step 4: Press the login button
    login.press_login_button()

    # Step 5: Verify error message for wrong credentials
    login.validate_login_error_message(test_data["Messages"]["WrongDataMessage"])


# E2E test: Login with locked-out user
def test_login_user_locked(page):
    # Step 1: Initialize page objects
    login = LoginPage(page)

    # Step 2: Navigate to the login page
    page.goto(test_data["Endpoint"])

    # Step 3: Fill in the login form with locked-out username
    login.fill_input("username", test_data["Users"]["LockedUser"]["Username"])
    login.fill_input("password", test_data["Users"]["LockedUser"]["Password"])

    # Step 4: Press the login button
    login.press_login_button()

    # Step 5: Verify error message for locked user
    login.validate_login_error_message(test_data["Messages"]["LockedUserMessage"])
