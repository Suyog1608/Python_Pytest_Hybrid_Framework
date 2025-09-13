from selenium.webdriver.common.by import By


class LoginPage:
    username_field = (By.NAME, "user_name")
    password_field = (By.NAME, "user_password")
    login_button = (By.NAME, "Login")
    logo_image = (By.XPATH, "//img[@src='include/images/vtiger-crm.gif']")
    Error_msg = (By.XPATH, "//*[contains(text(), 'You must specify a valid username and password')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.setUserId(username)
        self.setUserPass(password)
        self.click_login()

    def setUserId(self, username):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def setUserPass(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def verify_errorMssg(self):
        try:
            return self.driver.find_element(*self.Error_msg).is_displayed()
        except:
            return False

    def verify_Logo(self):
        try:
            return self.driver.find_element(*self.logo_image).is_displayed()
        except:
            return False
