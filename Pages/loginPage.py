from selenium.webdriver.common.by import By
from utils.commonActions import CommonMethod


class LoginPage(CommonMethod):

    def __init__(self, driver):
        super().__init__(driver)

    username_field = (By.NAME, "user_name")
    password_field = (By.NAME, "user_password")
    login_button = (By.NAME, "Login")
    logo_image = (By.XPATH, "//img[@src='include/images/vtiger-crm.gif']")
    Error_msg = (By.XPATH, "//*[contains(text(), 'You must specify a valid username and password')]")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.setUserId(username)
        self.setUserPass(password)
        self.click_login()

    def setUserId(self, username):
        # self.driver.find_element(*self.username_field).clear()
        # self.driver.find_element(*self.username_field).send_keys(username)
        self.setInput(self.username_field, username)

    def setUserPass(self, password):
        # self.driver.find_element(*self.password_field).clear()
        # self.driver.find_element(*self.password_field).send_keys(password)
        self.setInput(self.password_field, password)

    def click_login(self):
        # self.driver.find_element(*self.login_button).click()
        self.clickElement(self.login_button)

    def verify_errorMssg(self):
        try:
            # return self.driver.find_element(*self.Error_msg).is_displayed()
            return self.checkDisplay(self.Error_msg)
        except:
            return False

    def verify_Logo(self):
        try:
            # return self.driver.find_element(*self.logo_image).is_displayed()
            return self.checkDisplay(self.logo_image)
        except:
            return False
