from playwright.sync_api import sync_playwright

# Test for validating the POST request to create a new post via an API (jsonplaceholder.typicode.com)

# Test data initialization
restApiUrl = "https://jsonplaceholder.typicode.com/"
path = "posts"
requestBody = {
    # Data to be sent in the POST request body
    "title": "testTitle",
    "body": "bodyTitle",
    "userId": 1,
}


def test_post_posts():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Step 1: Send POST request to create a new post
        postDataResponse = request_context.post(
            f"{restApiUrl}{path}",  # Concatenate the base URL with the 'posts' endpoint
            data=requestBody,  # Send the request body with the data for the new post
            headers={
                "Content-Type": "application/json; charset=UTF-8"  # Set the correct Content-Type header for JSON data
            },
        )

        # Step 2: Verify the status of the API response
        assert (
            postDataResponse.ok
        )  # Assert that the request was successful (status code 2xx)
        assert (
            postDataResponse.status == 201
        )  # Assert that the status code is 201 (Created)

        # Step 3: Parse the JSON response body
        responseBody = (
            postDataResponse.json()
        )  # Convert the response body to JSON format
        print(responseBody)
        # Print the response body for debugging purposes

        # Step 4: Validate the response data
        # Validate that the userId in the response matches the request body
        assert responseBody["userId"] == requestBody["userId"]
        assert "userId" in responseBody
        assert isinstance(responseBody["userId"], int)

        # Validate that the title in the response matches the title sent in the request body
        assert responseBody["title"] == requestBody["title"]
        assert "title" in responseBody
        assert isinstance(responseBody["title"], str)

        # Validate that the body in the response matches the body sent in the request body
        assert responseBody["body"] == requestBody["body"]
        assert isinstance(responseBody["body"], str)
