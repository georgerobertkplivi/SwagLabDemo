from seleniumbase import BaseCase

class ProductListPage(BaseCase):
    add_to_cart_backpack = "*[data-test=\"add-to-cart-sauce-labs-backpack\"]"
    shopping_cart_badge = "#item_4_title_link > .inventory_item_name"
    product_sort_container = "*[data-test=\"product_sort_container\"]"
    product_page_title =  ".title"
    product_link = "//div[.='Sauce Labs Backpack']"
    back_to_product = "*[data-test=\"back-to-products\"]"

# Actionable Methods
    def AddProductToCart(self):
        self.click(self.add_to_cart_backpack)

    def Click_Back_To_Product_Button(self):
        self.click(self.back_to_product)

    def ClickShoppingCartBadge(self):
        self.click(self.shopping_cart_badge)

    def ClickSortDropDown(self,dropdown_option):
        self.select_option_by_text(self.product_sort_container,dropdown_option)

    def Click_product(self):
        self.click(self.product_link)


# Non Actionable Methods
    def GetProductPageTitle(self):
        self.assert_element(self.product_page_title)

    def Verify_Product_Details_Page(self):
        self.assert_element(self.back_to_product)