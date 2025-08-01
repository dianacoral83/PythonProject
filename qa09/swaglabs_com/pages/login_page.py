from qa09.playwright.MyFirstPlaywright import login_button


class loginPage():
    def login(self,user_text,password_text):
        login_button=self.page.get_by_text("Login")
        user.fill(user_text)
        password.fill(password_text)
        login_button.click()

        def verify_login_success(self):
            url=self.page.url
            assert url=="https://www.saucedemo.com/inventory.html,"

        def verify_login_fail(self):
            url=self.page.url
            assert url=="https://www.saucedemo.com/inventory.html,"

class loginPage():
    def login(self,user_text,password_text):
        login_button=self.page.get_by_text("Login")
        user.fill(user_text)
        password.fill(password_text)
        login_button.click()

        def verify_login_success(self):
            url=self.page.url
            assert url=="https://www.saucedemo.com/inventory.html,"

        def verify_login_fail(self):
            url=self.page.url
            assert url=="https://www.saucedemo.com/inventory.html,"

