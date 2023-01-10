from Userinfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class Github:
    def __init__(self,username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    #methods
    def signIn(self):
        self.browser.get("https://github.com/login")
        Username= self.browser.find_element(By.XPATH,'//*[@id="login_field"]')
        time.sleep(2)
        Username.send_keys(self.username)
        time.sleep(2)
        Password= self.browser.find_element(By.XPATH,'//*[@id="password"]')
        time.sleep(2)
        Password.send_keys(self.password)
        time.sleep(2)

        self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[11]').click()

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)
        
        items = self.browser.find_elements(By.CSS_SELECTOR, '[data-hovercard-type="user"]')
        """items= self.browser.find_elements(By.CLASS_NAME,"d-inline-block no-underline mb-1")"""

        for i in items:
           print(i.text)


github=Github(username,password)
github.signIn()
github.getFollowers()

