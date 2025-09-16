from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class CommonMethod:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setInput(self, locator, value):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            print(f"Timeout: Element not found for input: {locator}")
            raise
        except NoSuchElementException:
            print(f"NoSuchElementException: {locator}")
            raise

    def clickElement(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.click()
        except TimeoutException:
            print(f"Timeout: Element not clickable: {locator}")
            raise
        except NoSuchElementException:
            print(f"Element Not Found: {locator}")
            raise

    def checkDisplay(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.is_displayed()
        except Exception:
            print(f"Element Not found {locator}")
            raise