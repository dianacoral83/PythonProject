

def test_home_page(setup_playwright):
    page = setup_playwright
    page.goto("https://airbnb.com")
    page.wait_for_timeout(5000)
    assert "airbnb.com" in page.url

def test_find_city(setup_playwright):
    page = setup_playwright
    page.goto("https://airbnb.com")
    page.wait_for_load_state("load")
    page.wait_for_timeout(3000)
    element = page.locator("text=Где")
    assert element.first.is_visible()
    element.click()
    page.wait_for_timeout(1000)
    input_field = page.locator("input[placeholder='Поиск направлений']")
    input_field.fill("Tokyo")
    page.locator("[data-testid='structured-search-input-search-button']").click()
    assert "/s/Tokyo" in page.url
    page.wait_for_timeout(3000)
    page.locator("text=Кто едет?").click()
    page.wait_for_timeout(2000)
    page.locator('[data-testid="stepper-adults-increase-button"]').first.click()
    page.wait_for_timeout(1000)
    # Get the value after clicking
    adult_value = page.locator('[data-testid="stepper-adults-value"]').first.text_content()
    # Assert that it's "1"
    assert adult_value.strip() == "1"


