from playwright.sync_api import sync_playwright

# Test data initialization
restApiUrl = "https://jsonplaceholder.typicode.com/"
path = "users"
notExistedPath = "userstest"
expectedName = "Kurtis Weissnat"
expectedUsername = "Elwyn.Skiles"
expectedCity = "Howemouth"
expectedCompanyName = "Johns Group"
expectedCatchPhrase = "Configurable multimedia task-force"

# Test for validating the GET request for a user through an API (using jsonplaceholder.typicode.com)


def test_get_user():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Step 1: Send GET request to the users API
        response = request_context.get(
            f"{restApiUrl}{path}/7", headers={"Accept": "application/json"}
        )

        # Step 2: Verify the status of the API response
        assert response.ok
        assert response.status == 200

        # Step 3: Parse the JSON response body
        response_body = response.json()
        print(response_body)

        # Step 4: Validate the response data

        # Validate the user's name
        assert "name" in response_body
        assert response_body["name"] == expectedName

        # Validate the username field
        assert response_body["username"] == expectedUsername
        assert isinstance(response_body["username"], str)

        # Validate the address - specifically the city
        assert response_body["address"]["city"] == expectedCity

        # Validate the company name
        assert response_body["company"]["name"] == expectedCompanyName

        # Validate the company catchphrase
        assert response_body["company"]["catchPhrase"] == expectedCatchPhrase

        # Validate id type
        assert isinstance(response_body["id"], int)


# Test to validate the GET request for a non-existent path (404 Not Found)


def test_get_user_not_found():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Step 1: Send a GET request to the users API with a non-existent path
        userDataStatus = request_context.get(
            f"{restApiUrl}{notExistedPath}/7", headers={"Accept": "application/json"}
        )
        # Step 2: Assert that the status code is 404 (Not Found)
        assert userDataStatus.status == 404
