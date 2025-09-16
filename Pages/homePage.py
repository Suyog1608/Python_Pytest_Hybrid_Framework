from selenium.webdriver.common.by import By
from utils.commonActions import CommonMethod


class HomePage(CommonMethod):

    def __init__(self, driver):
        # self.driver = driver
        super().__init__(driver)

    home_link = (By.LINK_TEXT, "Home")
    logout_link = (By.LINK_TEXT, "Logout")
    NewLead_link = (By.LINK_TEXT, "New Lead")

    def verifyHome(self):
        # return self.driver.find_element(*self.home_link).is_displayed()
        return self.checkDisplay(self.home_link)

    def verifyLogout(self):
        # return self.driver.find_element(*self.logout_link).is_displayed()
        return self.checkDisplay(self.logout_link)

    def click_logout(self):
        # self.driver.find_element(*self.logout_link).click()
        self.clickElement(self.logout_link)

    def click_NewLead(self):
        self.clickElement(self.NewLead_link)