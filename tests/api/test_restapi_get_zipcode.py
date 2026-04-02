from playwright.sync_api import sync_playwright

# Test data initialization
rest_api_url = "https://api.zippopotam.us/"
country_code = "us"
zip_code = 28270
not_existed_zip_code = 11111
country = "United States"
state_code = "NC"
state_name = "North Carolina"
city = "Charlotte"


def test_get_zipcode():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Step 1: Send GET request
        response = request_context.get(
            f"{rest_api_url}{country_code}/{zip_code}",
            headers={"Accept": "application/json"},
        )

        # Step 2: Verify status
        assert response.ok
        assert response.status == 200

        # Step 3: Parse JSON
        response_body = response.json()
        print(response_body)

        # Step 4: Validate response data
        assert response_body["country"] == country
        assert "country" in response_body
        assert isinstance(response_body["country"], str)
        assert response_body["places"][0]["place name"] == city
        assert response_body["places"][0]["state abbreviation"] == state_code
        assert response_body["places"][0]["state"] == state_name
        assert isinstance(response_body["places"][0]["state"], str)


def test_get_zipcode_not_found():
    with sync_playwright() as p:
        request_context = p.request.new_context()

        # Step 1: Send GET request for non-existing zip
        response = request_context.get(
            f"{rest_api_url}{country_code}/{not_existed_zip_code}",
            headers={"Accept": "application/json"},
        )

        # Step 2: Verify 404
        assert response.status == 404
