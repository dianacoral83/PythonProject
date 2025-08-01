from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[id='user-name']")
    user = page.locator("[id='user-name']")
    page.locator("[id='password']")
    password = page.locator("[id='password']")
    page.locator("[id='login-button']")
    login_button= page.get_by_text("Login")
    login_button_by_name = page.locator("[name='login-button']") # example for name
    user.fill("standard_user")
    password.fill("secret_sauce")
    login_button.click()
    url = page.url
    expted_url = "https://www.saucedemo.com/inventory.html"
    if (url == expted_url):
        print("Login Success url found as expected")

    page.close()
    browser.close()
    print("### Test end ###")