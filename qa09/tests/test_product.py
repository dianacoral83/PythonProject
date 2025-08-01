

class test_product:
    def test_login_correct_parameters(self, setup_swaglabs):
        page, login_page, product_page = setup_swaglabs
        login_page.login("standart_user", "secret_sauce")
        product_page.verify_product_price

