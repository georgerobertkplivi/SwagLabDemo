from seleniumbase import BaseCase

from Commons.commons import Commons
from Pages.HomePage import HomePage

class Login(BaseCase):
        # All Login Page Locators
        login_logo = ".login_logo"
        bot_logo = ".bot_column"
        username_field = "*[data-test=\"username\"]"
        password_field = "*[data-test=\"password\"]"
        login_button = "*[data-test=\"login-button\"]"
        error_msg = "*[data-test=\"error\"]"
        product_page_title = ".title"
        add_to_cart = "*[data-test=\"add-to-cart-sauce-labs-backpack\"]"
        shopping_cart = ".shopping_cart_badge"
        checkout_button = "*[data-test=\"checkout\"]"
        item_name_in_cart = ".inventory_item_name"
        item_name = "#item_4_title_link > .inventory_item_name"

        # Check Out Form Locator
        fname = "*[data-test=\"firstName\"]"
        lname = "*[data-test=\"lastName\"]"
        postalcode = "*[data-test=\"postalCode\"]"
        continue_button = "*[data-test=\"continue\"]"
        finish_button = "*[data-test=\"finish\"]"
        back_to_products_button = "*[data-test=\"back-to-products\"]"
        thank_you_msg = ".complete-header"

        # Data from Commons utility file
        page_url = Commons.url

        # All Actions that can be Performed on Home Page are here

        # Open Web Page or Desire URL
        def load_page(self):
            self.open(self.page_url)

        # Home Page Actions
        def clickLoginButton(self):
            self.click(self.login_button)

        def setUsername(self, username):
            self.type(self.username_field, username)

        def setPassword(self, password):
            self.type(self.password_field, password)

        def setFirstname(self, firstname):
            self.type(self.fname, firstname)

        def setLastname(self, lastname):
            self.type(self.lname, lastname)

        def setPostalCode(self, postcode):
            self.type(self.postalcode, postcode)

        def clickCart(self):
            self.click(self.shopping_cart)

        def clickCheckOut(self):
            self.click(self.checkout_button)

        def clickContinueButton(self):
            self.click(self.continue_button)

        def clickBackButton(self):
            self.click(self.back_to_products_button)

        # Login Page Methods

        def log_in(self, username, password):
            self.setUsername(username)
            self.setPassword(password)
            self.clickLoginButton()




