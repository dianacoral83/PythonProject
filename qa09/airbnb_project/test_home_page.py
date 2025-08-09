from qa09.airbnb_project.conftest import setup_playwright


class TestLogin():

    base_url = "https://www.airbnb.com/?locale=en&currency=USD"

    # Locators
    find_path = "[data-testid='structured-search-input-field-query']"
    search_button = "[data-testid='structured-search-input-search-button']"
    adults_increase_button = '[data-testid="stepper-adults-increase-button"]'
    adults_value = '[data-testid="stepper-adults-value"]'

    def test_home_page(self, setup_playwright):
        page = setup_playwright
        page.goto(self.base_url)
        page.wait_for_timeout(5000)
        assert "airbnb.com" in page.url

    def test_find_city(self, setup_playwright):
        page = setup_playwright
        page.goto(self.base_url)
        page.wait_for_load_state("load")
        page.wait_for_timeout(2000)
        page.locator("text=Where").click()
        #assert element.first.is_visible()
        page.wait_for_timeout(1000)
        page.locator(self.find_path).fill("Tokyo, Japan")
        page.locator('b:has-text("Tokyo")').first.click()
        #assert "/s/Tokyo" in page.url
        #page.wait_for_timeout()
        page.locator('text="Add guests"').click()
        #page.locator("text=Who?").click()
        page.wait_for_timeout(1000)
        page.locator(self.adults_increase_button).first.click()
        page.wait_for_timeout(1000)
        # Get the value after clicking
        adult_value = page.locator(self.adults_value).first.text_content()
        # Assert that it's "1"
        assert adult_value.strip() == "1"

    def test_services_url(self, setup_playwright):
        page = setup_playwright
        page.goto(self.base_url)
        page.wait_for_timeout(2000)
        assert "services" in page.url

    def test_go_to_experiences_tokyo(self, setup_playwright):
        page = setup_playwright
        page.goto(self.base_url)
        page.wait_for_selector("span[data-title='Experiences']").click()
        assert "experiences" in page.url
        assert page.inner_text("span[data-title='Experiences']").strip() == "Experiences"

    def test_click_experiences_multi_lang(self, setup_playwright):
        page = setup_playwright
        page.goto(self.base_url)
        page.locator("span[data-title='Homes']").click()
        assert "homes" in page.url


