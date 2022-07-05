import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    login_email_id ='Email'
    login_password_id = 'Password'
    btn_login_xpath ='/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'

    def __init__(self,driver):
        self.driver = driver
    def login_Credentials_Username(self,username):

        self.driver.find_element(by=By.ID,value=self.login_email_id).clear()
        time.sleep(3)
        self.driver.find_element(by=By.ID,value=self.login_email_id).send_keys(username)

    def login_Credentials_password(self,password):
        time.sleep(3)
        self.driver.find_element(by=By.ID,value=self.login_password_id).clear()
        time.sleep(3)
        self.driver.find_element(by=By.ID,value=self.login_password_id).send_keys(password)

    def btn_click_login(self):
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=self.btn_login_xpath).click()



