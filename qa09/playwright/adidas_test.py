from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    page.locator(".gh-search-button__advanced-link").click()

    page.wait_for_url("**/sch/ebayadvsearch*", timeout=5000)

    if "ebayadvsearch" in page.url:
        print(f"success {page.url}")

