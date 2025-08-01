
class TestSwaglabs():
# def - saved word for function
# test - mandatory
    def test_login_correct_user(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        prices_elements = page.locator(".inventory_item_price")
        count = prices_elements.count()
        assert count > 0, "לא נמצאו מחירים בדף"

        for i in range(count):
            price_text = prices_elements.nth(i).inner_text()  # דוגמה: "$29.99"
            price = float(price_text.replace("$", ""))
            print(f"🔍 מוצר {i + 1}: ${price}")
            assert price < 100, f"❌ מחיר גבוה מדי: ${price}"

        print("✅ כל המחירים נמוכים מ־$100")
        print("Trying to login with correct parameters ")


    def test_login_incorrect_user(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.saucedemo.com/")
        print("Trying to login with incorrect parameters ")

