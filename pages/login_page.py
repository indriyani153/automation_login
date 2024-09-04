from selenium.webdriver.common.by import By
from locators.login_locator import LoginLocator

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(By.ID, LoginLocator.username).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.ID, LoginLocator.password).send_keys(password)

    def click_button_login(self):
        self.driver.find_element(By.XPATH, LoginLocator.button_login).click()

    def success(self):
        show = self.driver.find_element(By.ID, LoginLocator.success_message).is_enabled() == True
        return show
    
    def failed(self):
        show = self.driver.find_element(By.ID, LoginLocator.error_message).is_enabled() == True
        return show