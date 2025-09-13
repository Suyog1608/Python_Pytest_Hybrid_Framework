from selenium.webdriver.common.by import By


class HomePage:
    home_link = (By.LINK_TEXT, "Home")
    logout_link = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def verifyHome(self):
        return self.driver.find_element(*self.home_link).is_displayed()

    def verifyLogout(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()