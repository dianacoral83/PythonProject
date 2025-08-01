

class TestLogin():

    def test_login_correct_parameters(self, setup_playwright):
        page, login_page, product_page = setup_swaglabs
        login_page.login("standart_user", "secret_sauce")

    def test_login_incorrect_user(self, setup_swaglabs):
        page, login_page, product_page = setup_swaglabs
