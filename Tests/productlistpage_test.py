from Pages.ProductListPage import ProductListPage
from Pages.HomePage import HomePage
from Commons.commons import Commons

class ProductListPage(ProductListPage, HomePage):
    # Drop Down Options By Text
    dropdown_a_z = "Name (A to Z)"
    dropdown_z_a = "Name (Z to A)"
    dropdown_high_low = "Price (high to low)"
    dropdown_low_high = "Price (low to high)"


    def test_TC0012_View_product_list(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user,  Commons.valid_password)
        # Assert or Verify Product List Page
        self.GetProductPageTitle()


    def test_TC0013_View_product_detail(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Product Name to View Product Details
        self.Click_product()
        # Assert or Verify Product Details Page
        self.Verify_Product_Details_Page()

    def test_TC0014_Tap_back_in_product_detail_page(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Product Name to View Product Details
        self.Click_product()
        # Click back to product button
        self.Click_Back_To_Product_Button()
        # Assert or Verify Product Page
        self.GetProductPageTitle()

    def test_TC0015_Sort_product_list_by_name_A_to_Z(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Dropdown menu and select Name A to Z
        self.ClickSortDropDown(self.dropdown_a_z)

    def test_TC0016_Sort_product_list_by_name_Z_to_A(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Dropdown menu and select Name Z to A
        self.ClickSortDropDown(self.dropdown_z_a)

    def test_TC0017_Sort_product_list_by_Price_Low_to_High(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Dropdown menu and select Price Low to High
        self.ClickSortDropDown(self.dropdown_low_high)

    def test_TC0018_Sort_product_list_by_Price_High_to_Low(self):
        # Load Website
        self.load_page()
        # Login to Website
        self.login(Commons.standard_user, Commons.valid_password)
        # Click on Dropdown menu and select Price High to Low
        self.ClickSortDropDown(self.dropdown_high_low)
