from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Swag_Labs:
    # username & password data
    username = "standard_user"
    password = "secret_sauce"

    # Locators Data

    username_locator = "user-name"
    password_locator = "password"
    login_locator = "login-button"
    web_page_content_locator = "//body"


    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return False

    def get_cookies(self):

        cookies_before_login = self.driver.get_cookies()
        print(cookies_before_login)
        self.driver.find_element(by=By.NAME,value=self.username_locator).send_keys(self.username)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.NAME,value=self.login_locator).click()
        sleep(2)
        cookies_after_login = self.driver.get_cookies()
        print(cookies_after_login)

if __name__ == "__main__":
    url = "https://www.saucedemo.coms/"
    sauce_labs = Swag_Labs(url)
    sauce_labs.get_cookies()