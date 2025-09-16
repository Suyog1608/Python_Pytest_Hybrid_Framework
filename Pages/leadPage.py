from selenium.webdriver.common.by import By
from utils.commonActions import CommonMethod


class leadPage(CommonMethod):

    def __init__(self, driver):
        super().__init__(driver)

    lastname_input = (By.NAME, "lastname")
    company_input = (By.NAME, "company")
    save_button = (By.NAME, "button")

    def setLastname(self, lname):
        self.setInput(self.lastname_input, lname)

    def setCompany(self, comp):
        self.setInput(self.company_input, comp)

    def click_Save(self):
        self.clickElement(self.save_button)

    def create_lead(self, lname, comp):
        self.setLastname(lname)
        self.setCompany(comp)
        self.click_Save()