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
    menu_button_locator = "react-burger-menu-btn"
    logout_locator = "Logout"

    
    def __init__(self,url):
        # Initialize the class with the URL and set up the Chrome driver
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        # Start the browser automation process
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return False

    def get_cookies(self):
        # Get cookies before and after login and perform login/logout actions
        cookies_before_login = self.driver.get_cookies()
        print("Cookies before Login:\n", cookies_before_login)
        
        # Find username field and input the username
        self.driver.find_element(by=By.NAME,value=self.username_locator).send_keys(self.username)
        sleep(2)
        
        # Find password field and input the password
        self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)
        sleep(2)

        # Find and click the login button
        self.driver.find_element(by=By.NAME,value=self.login_locator).click()
        sleep(2)

        # Get cookies after login
        cookies_after_login = self.driver.get_cookies()
        print("Cookies after Login:\n", cookies_after_login)

        # Find and click the menu button
        self.driver.find_element(by=By.ID,value=self.menu_button_locator).click()
        sleep(2)

        # Find and click the logout button
        self.driver.find_element(by=By.LINK_TEXT,value=self.logout_locator).click()
        sleep(2)

# main program
if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    sauce_labs = Swag_Labs(url)
    sauce_labs.start_automation()
    sauce_labs.get_cookies()