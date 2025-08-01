from asyncio import wait_for


class TestPlay:

    def test_ebay_navigation(self,setup_playwright):
       page=setup_playwright
       page.goto("https://www.ebay.com/sch/i.html?_nkw=shoes&_sacat=0&_from=R40&_trksid=m570.l1313")
       page.locator("#item474e9680cb").click()
       print("")
