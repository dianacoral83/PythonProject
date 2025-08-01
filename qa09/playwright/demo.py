

from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.guru99.com/test/newtours/index.php")
    page.locator('[name="userName"]').fill("tutorial")
    page.locator('[name="password"]').fill("tutorial")
    page.locator('[name="submit"]').click()
    page.wait_for_timeout(2000)
    if page.locator("text=Login Successfully").is_visible():
        print("Login successful!")
    else:
        print("Login failed. Stay on:", page.url)
