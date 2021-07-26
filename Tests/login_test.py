from Commons.commons import Commons
from Pages.HomePage import HomePage
from Pages.Login import Login

class LoginTest(Login, HomePage):
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

    # Data
    invalid_login_err = "Epic sadface: Username and password do not match any user in this service"
    locked_user_err = "Epic sadface: Sorry, this user has been locked out."

    # Locators
    login_err_msg = "*[data-test='error']"

    def test_TC0008_Input_valid_username_and_valid_password(self):
        self.load_page()
        self.login(self.standard_user, self.password)

    def test_TC0009_Input_valid_username_and_invalid_password(self):
        self.load_page()
        self.login(self.standard_user, self.password_invalid)
        self.login_err_text = self.get_text(self.login_err_msg)
        self.assert_equal(self.invalid_login_err, self.login_err_text)

    # def test_TC0010_Input_invalid_username_and_valid_password(self):
    #     pass
    #
    # def test_TC0011_Input_invalid_username_and_invalid_password(self):
    #     pass

    def test_TC00029_loginPageLoginUnsuccessLockedOutUser(self):
        self.load_page()
        self.log_in(self.locked_user, self.password)
        self.assert_text(self.locked_user_err,self.error_msg)
