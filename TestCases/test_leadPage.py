import pytest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.leadPage import leadPage
from utils.read_excel import read_excel_as_dict_of_dicts
from utils.read_ini import get_ini_data

login_data_dict = read_excel_as_dict_of_dicts("TestData/testdata.xlsx", "LoginData")


@pytest.mark.usefixtures("browser")
class Test_leadPage:

    def test_create_lead_TC05(self):
        row = login_data_dict["test_create_lead_TC05"]
        lname = row["lastname"]
        comp = row["company"]
        lp = LoginPage(self.driver)
        lp.login(get_ini_data('AppData', 'username'), get_ini_data('AppData', 'password'))
        hp = HomePage(self.driver)
        assert hp.verifyHome() == True
        hp.click_NewLead()
        ldp = leadPage(self.driver)
        ldp.create_lead(lname,comp)
        hp.click_logout()