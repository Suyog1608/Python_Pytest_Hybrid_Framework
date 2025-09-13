import pytest
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage


@pytest.mark.usefixtures("browser")
class Test_loginPage:
    def test_verifyTitle_TCO1(self):
        assert self.driver.title == "vtiger CRM - Commercial Open Source CRM"

    def test_verifyLogo_TC02(self):
        lp = LoginPage(self.driver)
        assert lp.verify_Logo() == True

    def test_verify_invalidLogin_TC03(self):
        lp = LoginPage(self.driver)
        lp.login("admin12", "admin")
        assert lp.verify_errorMssg() == False

    def test_verify_validLogin_TC04(self):
        lp = LoginPage(self.driver)
        lp.login("admin", "admin")
        hp = HomePage(self.driver)
        assert hp.verifyHome() == True
