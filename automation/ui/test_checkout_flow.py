def test_checkout_flow(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add product and go to cart
    page.click("text=Add to cart")
    page.click(".shopping_cart_link")

    # Start checkout
    page.click("text=Checkout")

    # Should be on checkout page
    assert "checkout-step-one" in page.url
