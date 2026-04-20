import requests
import pytest
from playwright.sync_api import sync_playwright

from pages.QuickPizza.homepage import Homepage
from test_data.QuickPizza.test_data import test_data

user_token = None


@pytest.fixture(scope="session", autouse=True)
def get_user_token():
    global user_token

    session = requests.Session()

    # 1. Request CSRF token from the server
    csrf_response = session.post(f'{test_data["Endpoint"]}api/csrf-token')

    # 2. Extract CSRF token from Set-Cookie header
    csrf_token = session.cookies.get("csrf_token")

    if not csrf_token:
        raise ValueError(f"Brak csrf_token w cookies: {session.cookies.get_dict()}")

    # 3. Login payload
    payload = {
        "username": test_data["UserCredentials"]["Username"],
        "password": test_data["UserCredentials"]["Password"],
        "csrf": csrf_token,
    }

    # 4. Perform login and retrieve user token
    login_response = session.post(
        f'{test_data["Endpoint"]}api/users/token/login?set_cookie=true',
        json=payload,
        headers={"Content-Type": "application/json", "X-Csrf-Token": csrf_token},
    )

    print("LOGIN RESPONSE:", login_response.json())

    user_token = login_response.json().get("token")

    if not user_token:
        raise ValueError(f"No token in response: {login_response.text}")


def test_provide_rating():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # 1. Add cookie
        context.add_cookies(
            [
                {
                    "name": "qp_user_token",
                    "value": user_token,
                    "domain": test_data["Endpoint"]
                    .replace("https://", "")
                    .replace("http://", "")
                    .strip("/"),
                    "path": "/",
                    "httpOnly": True,
                    "secure": True,
                    "sameSite": "Strict",
                }
            ]
        )

        page = context.new_page()
        homepage = Homepage(page)

        # 2. Wait for pizza API
        with page.expect_response(
            lambda r: "/api/pizza" in r.url
        ) as pizza_response_info:
            page.goto(test_data["Endpoint"])
            homepage.press_pizza_button()

        pizza_response = pizza_response_info.value
        assert pizza_response.status == 200

        # 3. Rate pizza
        homepage.press_recommend_rutton()
        homepage.validate_if_no_thanks_is_visible()

        # 4. Wait for rating response
        with page.expect_response(
            lambda r: "/api/ratings" in r.url
        ) as rating_response_info:
            pass

        rating_response = rating_response_info.value
        assert rating_response.status == 201

        # 5. Validate message
        homepage.validate_rating_message(test_data["RatingMessage"])

        # 6. Click "no thanks"
        with page.expect_response(
            lambda r: "/api/ratings" in r.url
        ) as rating_response_info2:
            homepage.press_no_thanks_button()

        rating_response2 = rating_response_info2.value
        assert rating_response2.status == 201

        browser.close()
