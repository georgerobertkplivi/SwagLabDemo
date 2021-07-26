from Pages.Checkout import Checkout
from Pages.HomePage import HomePage
from Commons.commons import Commons




class CheckoutTest(Checkout, HomePage):

    firstname = "George"
    lastname = "Robert Kplibs"
    postcode = "00133"
    emp_fname = ""
    emp_lname = ""
    emp_pcode = ""
    err_msg_fname = "Error: First Name is required"
    err_msg_lname = "Error: Last Name is required"


    def test_TC0019_Click_button_add_to_Cart_in_product_list(self):
       # Load Page
        self.load_page()
       # Login in the website
        self.login(Commons.standard_user,Commons.valid_password)
       # Add Item to cart
        self.Add_Item_To_Cart()
       # Assert that Cart is not Empty after Clicking on Add to Cart
        self.CheckItem_InCart()


    def test_TC0020_View_cart_list(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert that Cart is not Empty after Clicking on Add to Cart
        self.Cart()


    def test_TC0021_View_the_item_details_on_the_cart(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()

    def test_TC0022_Remove_items_on_the_cart(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()
        # remove item from the list
        self.Remove_Item()

    def test_TC0023_Click_button_checkout(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()
        # Click Check Out Button
        self.Click_CheckoutButton()

    def test_TC0024_Input_complete_buyer_data(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()
        # Click Check Out Button
        self.Click_CheckoutButton()
        # Fill in Buyer Details
        self.fillCheckoutForm(self.firstname, self.lastname, self.postcode)
        # Click Continue
        self.Click_Continue_Button()
        # Finish Button
        self.Click_FinishButton()


    def test_TC0025_Input_incomplete_buyer_data(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()
        # Click Check Out Button
        self.Click_CheckoutButton()
        # Fill in Buyer Details Without First Name
        self.fillCheckoutForm(self.emp_fname, self.lastname, self.postcode)
        self.Click_Continue_Button()
        # Assert First Error Message
        self.assert_text(self.err_msg_fname,self.checkout_err)



    # def test_TC0026_Finish_checkout(self):
    #     pass
    #
    def test_TC0027_Cancel_checkout(self):
        # Load Page
        self.load_page()
        # Login in the website
        self.login(Commons.standard_user, Commons.valid_password)
        # Add Item to cart
        self.Add_Item_To_Cart()
        # Assert product is in the cart
        self.isItemPresent()
        # Click Check Out Button
        self.Click_CheckoutButton()
        # Fill in Buyer Details
        self.fillCheckoutForm(self.firstname, self.lastname, self.postcode)
        self.Cancel_Checkout()

    # def test_TC0028_Checkout_without_items_in_cart(self):
    #     pass