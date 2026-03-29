from pages.QABrains.login import LoginPage
from test_data.QABrains.test_data import test_data


def test_login_into_account(page):
    login = LoginPage(page)

    # ---------------- Step 1: Open login page ----------------
    page.goto(test_data["Endpoint"])

    # ---------------- Step 2: Fill login form ----------------
    login.fill_email(test_data["Users"]["SuccessUser"]["Username"])
    login.fill_password(test_data["Users"]["SuccessUser"]["Password"])

    # ---------------- Step 3: Login ----------------
    login.press_login_button()

    # ---------------- Step 4: Wait for login success ----------------
    page.wait_for_selector("text=" + test_data["Messages"]["LoginSuccessMessage"])

    # ---------------- Step 5: Validate login success ----------------
    login.validate_login_success_message(test_data["Messages"]["LoginSuccessMessage"])

    # ---------------- Step 6: Logout ----------------
    login.press_logout_button()

    # ---------------- Step 7: Validate login button visible again ----------------
    login.validate_login_button_visible()
