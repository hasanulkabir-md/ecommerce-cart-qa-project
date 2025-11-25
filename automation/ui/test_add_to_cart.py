def test_add_product_to_cart(page):
    # Login
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Add product
    page.click("text=Add to cart")

    # Go to cart
    page.click(".shopping_cart_link")

    # Assert cart has item
    assert page.locator(".cart_item").count() == 1
