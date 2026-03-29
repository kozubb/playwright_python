from playwright.sync_api import Page
from pages.QABrains.register import RegisterPage
from test_data.QABrains.test_data import test_data


def test_register_account(page: Page):
    register_page = RegisterPage(page)

    # Prepare test data
    register_data = {
        "name": test_data["RegisterForm"]["Name"],
        "country": test_data["RegisterForm"]["Country"],
        "accountType": test_data["RegisterForm"]["AccountType"],
        "email": test_data["RegisterForm"]["Email"],
        "password": test_data["RegisterForm"]["Password"],
    }

    # Wait for backend response
    with page.expect_response(
        lambda response: "registration?registered=true" in response.url
        and response.status == 200
    ) as response_info:

        # Step 1: Open registration page
        register_page.open_register_page(test_data["Endpoint"])

        # Step 2: Fill form
        register_page.fill_register_form(register_data)

        # Step 3: Submit form
        register_page.submit_form()

    # Step 4: Validate backend response
    response = response_info.value
    assert response.status == 200

    # Step 5: Validate UI
    register_page.validate_registration_success(
        test_data["Messages"]["RegisterSuccessfulMessage"]
    )
