from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(" https://www.zara.com/il/en/")
    page.wait_for_timeout(2000)
    page.click('[data-qa-id="notify-help-center-click"]')
    page.wait_for_timeout(5000)
    if page.locator('h1', has_text="Help"):
        print("Login successful!")
    else:
        print("Login failed. Stay on:", page.url)
    print("")

