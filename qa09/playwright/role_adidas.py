from playwright.sync_api import sync_playwright

from qa09.playwright.demo import browser


def test_get_by_role(0)
     with sync_playwright() as playwright:
     browser = p.chromium.launch (headless=False)
     page=browser.new_page()
     page.goto("https://advantageonlineshopping.com/")
     time.sleep(4)
     page.get_by_role ("Link", name ="contact Name")
     time.sleep(4)
 search_box = page.get_by_role("textbox", name="Search")
    print("search_box.text")
    search_box.fill("shoes")
    search_box.press("Enter")

import re
import time

from playwright.sync_api import sync_playwright

def test_get_by_role():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.adidas.com/us")
        time.sleep(3)

    search_box = page.get_by_role("textbox", name="Search")

    search_box.fill("shoes")
    search_box.press("Enter")










