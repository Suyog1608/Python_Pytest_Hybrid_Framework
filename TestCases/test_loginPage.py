import pytest
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utils.read_excel import read_excel_as_dict_of_dicts

login_data_dict = read_excel_as_dict_of_dicts("TestData/testData.xlsx", "LoginData")


@pytest.mark.usefixtures("browser")
class Test_loginPage:
    def test_verifyTitle_TCO1(self):
        assert self.driver.title == "vtiger CRM - Commercial Open Source CRM"

    def test_verifyLogo_TC02(self):
        lp = LoginPage(self.driver)
        assert lp.verify_Logo() == True

    @pytest.mark.parametrize("TCName", login_data_dict.keys())
    def test_verify_invalidLogin_TC03(self,TCName):
        row = login_data_dict["test_verify_invalidLogin_TC03"]
        username = row["username"]
        password = row["password"]
        lp = LoginPage(self.driver)
        lp.login(username, password)
        assert lp.verify_errorMssg() == True

    def test_verify_validLogin_TC04(self):
        lp = LoginPage(self.driver)
        lp.login("admin", "admin")
        hp = HomePage(self.driver)
        assert hp.verifyHome() == True
