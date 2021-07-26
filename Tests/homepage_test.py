from Pages.HomePage import HomePage
from Commons.commons import Commons

class HomePageTest(HomePage):
    # Data from Commons utility file
    password = Commons.valid_password
    password_invalid = Commons.invalid_password
    standard_user = Commons.standard_user
    locked_user = Commons.locked_out_user
    problem_user = Commons.problem_user
    glitch_user = Commons.performance_glitch_user
    empty_password = Commons.empty_password
    empty_username = Commons.empty_username

    # Check Out Form Details
    First_Name = "George"
    Last_Name = "Robs"
    Postal_Code = "00211"

    # Calling External Methods
    hp = HomePage

    # Assertion Data
    username_require_err = "Epic sadface: Username is required"
    password_required_err = "Epic sadface: Password is required"
    locked_out_user_err = "Epic sadface: Sorry, this user has been locked out."
    product_page_title_text = "Products"
    cart_url = "https://www.saucedemo.com/cart.html"
    checkout_url = "https://www.saucedemo.com/checkout-step-one.html"
    checkout_step2_url = "https://www.saucedemo.com/checkout-step-two.html"
    checkout_complete_url = "https://www.saucedemo.com/checkout-complete.html"
    product_page_url = "https://www.saucedemo.com/inventory.html"

    # All Home Page Test Methods Go here
    def test_TC0001_verify_HomePage_Loads_Successfully(self):
        self.hp.load_page(self)
        self.assert_elements(self.hp.password_field, self.hp.username_field, self.hp.login_button, self.hp.login_logo, self.hp.bot_logo)

    def test_TC0002_verify_Login_Successfully(self):
        self.hp.load_page(self)
        self.hp.login(self, self.standard_user, self.password)

    def test_TC0003_verify_Login_unsuccessful_with_Empty_Username_and_Password(self):
        self.hp.load_page(self)
        self.hp.login(self, self.empty_username, self.empty_password)
        if self.username_require_err in self.get_text(self.hp.error_msg):
            self.assert_element(self.hp.error_msg)
        else:
            raise Exception("Locator Not Found")

    def test_TC0004_verify_Login_unsuccessful_with_Empty_Username_Only(self):
        self.hp.load_page(self)
        self.hp.login(self, self.empty_username, self.password)
        if self.username_require_err in self.get_text(self.hp.error_msg):
            self.assert_element(self.hp.error_msg)
        else:
            raise Exception("Locator Not Found")

    def test_TC0005_verify_Login_unsuccessful_with_Empty_Password_Only(self):
        self.hp.load_page(self)
        self.hp.login(self, self.standard_user, self.empty_password)
        if self.password_required_err in self.get_text(self.hp.error_msg):
            self.assert_element(self.hp.error_msg)
        else:
            raise Exception("Locator Not Found")

    def test_TC0006_verify_Login_unsuccessful_with_Locked_Username_Only(self):
        self.hp.load_page(self)
        self.hp.login(self, self.locked_user, self.password)
        if self.locked_out_user_err in self.get_text(self.hp.error_msg):
            self.assert_element(self.hp.error_msg)
        else:
            raise Exception("Locator Not Found")

    def test_TC0007_ItemSelected_In_Products_Page_IsSameAsItem_In_CompleteCustomerCheckoutTest(self):
        self.hp.load_page(self)
        self.hp.login(self, self.standard_user, self.password)
        # Product Page
        if self.product_page_url == self.get_current_url():
            item_name = self.get_text(self.item_name)
            self.click(self.hp.add_to_cart)
            self.click(self.hp.shopping_cart)
            item_description_in_cart = self.get_text(self.item_name_in_cart)
            self.click(self.hp.checkout_button)
            # Adding Item To cart
            if self.is_element_present(self.continue_button):

                # Filling Check Out form
                # Check Out Step 1
                if self.is_element_present(self.continue_button):
                    self.assert_equal(item_name,item_description_in_cart)
                    self.fill_checkout_form(self.First_Name,self.Last_Name,self.Postal_Code)
                    self.click(self.continue_button)
                    # Check Out Step 2
                    if self.is_element_present(self.finish_button):
                        self.assert_equal(self.get_current_url(),self.checkout_step2_url)
                        self.click(self.finish_button)
                        # Complete Check Out
                        if self.is_element_present(self.thank_you_msg):
                            complete_checkout_url = self.get_current_url()
                            self.assert_equal(complete_checkout_url, self.checkout_complete_url)
                            self.click(self.back_to_products_button)
                            self.assert_equal(self.get_current_url(), self.product_page_url)
                    else:
                        raise Exception()

                else:
                    raise Exception("Element not found")
            else:
                raise Exception("Not on Check Out Info Page")
        else:
            raise Exception()


