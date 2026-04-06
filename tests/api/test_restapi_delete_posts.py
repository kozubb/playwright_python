from playwright.sync_api import sync_playwright

# Test for validating the DELETE request to remove a post via an API (jsonplaceholder.typicode.com)

# Test data initialization
restApiUrl = "https://jsonplaceholder.typicode.com/"
path = "posts"

postId = 1  # ID of the post to delete (for example, we are deleting post with ID 1)


def test_delete_posts():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        # Step 1: Send DELETE request to remove the existing post
        deletePostResponse = request_context.delete(
            f"{restApiUrl}{path}/{postId}"  # Concatenate the base URL with the 'posts' endpoint and post ID
        )

        # Step 2: Verify the status of the API response
        assert (
            deletePostResponse.ok
        )  # Assert that the request was successful (status code 2xx)
        assert (
            deletePostResponse.status == 200
        )  # Assert that the status code is 200 (OK) for successful deletion
