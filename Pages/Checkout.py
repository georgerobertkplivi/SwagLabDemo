from seleniumbase import BaseCase

class Checkout(BaseCase):
    # Check Out Form Locator
    shop_cart = ".shopping_cart_link"
    add_to_cart = "*[data-test=\"add-to-cart-sauce-labs-backpack\"]"
    fname = "*[data-test=\"firstName\"]"
    lname = "*[data-test=\"lastName\"]"
    postalcode = "*[data-test=\"postalCode\"]"
    continue_button = "*[data-test=\"continue\"]"
    finish_button = "*[data-test=\"finish\"]"
    shoppingCart = ".shopping_cart_badge"
    checkoutButton = "*[data-test=\"checkout\"]"
    back_to_products_button = "*[data-test=\"back-to-products\"]"
    thank_you_msg = ".complete-header"
    thank_you_msg_loc = "//h2[@class='complete-header']"
    cart_title = "//span[@class='title']"
    remove_button = "//button[@id='remove-sauce-labs-backpack']"
    checkout_err = "h3"
    cancel_button = "#cancel"
    continue_shopping = "#continue-shopping"




    # other resources
    cart_url = "https://www.saucedemo.com/cart.html"
    item_in_cart ="//div[@class='inventory_item_name']"
    product_page_url = "https://www.saucedemo.com/inventory.html"
    item_name_in_cart = ".inventory_item_name"
    item_name = "#item_4_title_link > .inventory_item_name"

# Actionable Methods
    def fillCheckoutForm(self, fname, lname, pcode):
        #self.clear(self.fname)
        self.setFirstname(fname)
        #self.clear(self.lname)
        self.setLastname(lname)
        #self.clear(self.pcode)
        self.setPostalCode(pcode)

    def ClearCheckoutForm(self):
        self.clear(self.fname)
        self.clear(self.lname)
        self.clear(self.postalcode)

    def Click_Cancel_Button(self):
        self.click(self.cancel_button)

    def Cancel_Checkout(self):
        self.Click_Cancel_Button()
        self.assert_element(self.continue_shopping)

    def Finish_Checkout(self):
        self.Click_Continue_Button()
        self.Click_FinishButton()
        self.assert_element(self.thank_you_msg_loc)

    def Remove_Item(self):
        self.click(self.remove_button)
        if self.is_element_present(self.remove_button) == False:
            pass
        else:
            raise  Exception("Some Items are still in the Cart")

    def Click_CheckoutButton(self):
        self.click(self.checkoutButton)

    def GoBack_To_Product_Page(self):
        self.click(self.back_to_products_button)

    def Click_FinishButton(self):
        self.click(self.finish_button)

    def Click_Continue_Button(self):
        self.click(self.continue_button)

    def setFirstname(self,firstname):
        self.type(self.fname, firstname)

    def setLastname(self, lastname):
        self.type(self.lname, lastname)

    def setPostalCode(self, postcode):
        self.type(self.postalcode, postcode)

    def Click_Cart_Button(self):
        self.click(self.shop_cart)

    def Add_Item_To_Cart(self):
        self.GetItemName()
        self.click(self.add_to_cart)
        self.Click_Cart_Button()

# Non Actionable Methods

    def CheckItem_InCart(self):
        shop_cart_url = self.get_current_url()
        if shop_cart_url == self.cart_url:
            self.assert_element(self.item_in_cart)
        else:
            raise Exception("Currently Not in Shopping Cart")

    def Cart(self):
        self.assert_element(self.cart_title)

    def GetItemName(self):
        product_name = self.get_text(self.item_name)
        return product_name

    def isItemPresent(self):
        if self.GetItemName() == self.get_text(self.item_in_cart):
            pass
        else:
            raise Exception("Item Does not Exist")



