test_data = {
    "Endpoint": "https://www.saucedemo.com",
    "CurrencySymbol": "$",
    "Tax": 0.08,
    "PaymentMethod": "SauceCard #31337",
    "DeliveryMethod": "Free Pony Express Delivery!",
    "Users": {
        "StandardUser": {
            "Username": "standard_user",
            "Password": "secret_sauce",
            "IncorrectPassword": "test_password",
        },
        "LockedUser": {
            "Username": "locked_out_user",
            "Password": "secret_sauce",
        },
        "OrderUser": {
            "FirstName": "Test First Name",
            "LastName": "Test Last Name",
            "Zipcode": "11111",
        },
    },
    "Products": {
        "Backpack": {
            "Name": "Sauce Labs Backpack",
            "Id": 4,
            "Price": 29.99,
        },
        "BikeLight": {
            "Name": "Sauce Labs Bike Light",
            "Id": 0,
            "Price": 9.99,
        },
    },
    "Messages": {
        "WrongDataMessage": "Username and password do not match any user in this service",
        "LockedUserMessage": "Sorry this user has been locked out.",
        "ThankYouMessage": "Thank you for your order!",
    },
    "CheckoutForm": {
        "FirstNameText": "First Name",
        "LastNameText": "Last Name",
        "ZipcodeText": "Zip/Postal Code",
    },
}
