from playwright.sync_api import sync_playwright

# Test for validating the PUT request to update a post via an API (jsonplaceholder.typicode.com)
# Test data initialization
restApiUrl = "https://jsonplaceholder.typicode.com/"
path = "posts"

# Data to be sent in the PUT request body for updating the post
updatedRequestBody = {
    "title": "updatedTitle",
    "body": "updatedBody",
    "userId": 1,
}

postId = 1  # ID of the post to update (for example, we are updating post with ID 1)


def test_put_posts():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        # Step 1: Send PUT request to update the existing post
        updatePostResponse = request_context.put(
            f"{restApiUrl}{path}/{postId}",  # Concatenate the base URL with the 'posts' endpoint and post ID
            data=updatedRequestBody,  # Send the updated data for the post
            headers={
                "Content-Type": "application/json; charset=UTF-8",  # Set the correct Content-Type header for JSON data
            },
        )

        # Step 2: Verify the status of the API response
        assert (
            updatePostResponse.ok
        )  # Assert that the request was successful (status code 2xx)
        assert (
            updatePostResponse.status == 200
        )  # Assert that the status code is 200 (OK) for successful update

        # Step 3: Parse the JSON response body
        responseBody = (
            updatePostResponse.json()
        )  # Convert the response body to JSON format
        print(responseBody)  # Print the response body for debugging purposes

        # Step 4: Validate the response data
        # Validate that the post ID in the response matches the requested post ID
        assert responseBody["id"] == postId
        assert "id" in responseBody
        assert isinstance(responseBody["id"], int)

        # Validate that the title in the response matches the updated title
        assert responseBody["title"] == updatedRequestBody["title"]
        assert "title" in responseBody
        assert isinstance(responseBody["title"], str)

        # Validate that the body in the response matches the updated body
        assert responseBody["body"] == updatedRequestBody["body"]
        assert "body" in responseBody
        assert isinstance(responseBody["body"], str)

        # Validate that the userId in the response matches the userId from the request body
        assert responseBody["userId"] == updatedRequestBody["userId"]
        assert "userId" in responseBody
        assert isinstance(responseBody["userId"], int)
