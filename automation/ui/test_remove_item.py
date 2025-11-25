def test_remove_product_from_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add then go to cart
    page.click("text=Add to cart")
    page.click(".shopping_cart_link")

    # Remove item
    page.click("text=Remove")

    # Cart should be empty
    assert page.locator(".cart_item").count() == 0
