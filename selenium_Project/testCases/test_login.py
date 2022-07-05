import time
import pytest
from selenium import webdriver
from pageObject.Loginpage import Login
from utilites.readProperties import readConfig
from utilites.custommLoger import logGen



class Test_001_Login():

    Base_URL = readConfig.getApplicationURL()
    username = readConfig.getUseremail()
    password =readConfig.getUserPassword()
    logger1= logGen.loggen()

    driver = webdriver.Chrome(executable_path=r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe")

    @pytest.fixture(scope='module')
    def setup(self):
        time.sleep(5)
        self.driver.get(self.Base_URL)
        time.sleep(3)
        self.driver.maximize_window()

    def test_initial (self,setup):
        self.logger1.info("***********Test_001_Login***********")
        self.logger1.info("***********Test case for html title***********")
        time.sleep(3)
        title = self.driver.title
        time.sleep(3)
        if((title == 'Your store. Login') and (self.driver.current_url == 'https://admin-demo.nopcommerce.com/login')):
            assert True
            self.logger1.info("***********Test case of title is passed***********")
        else:
            assert False
            self.logger1.info("***********Test case of title is failed***********")

    def test_usernamepassword(self,setup):
        self.logger1.info("***********Test case for login with username and password***********")
        log = Login(self.driver)
        time.sleep(3)
        log.login_Credentials_Username(self.username)
        time.sleep(3)
        log.login_Credentials_password(self.password)
        time.sleep(3)
        log.btn_click_login()
        time.sleep(3)
        if (self.driver.title == 'Dashboard / nopCommerce administration'):
            self.logger1.info("***********Test case of login is passed***********")
            assert True
            self.driver.close()
        else:
            self.logger1.info("***********Test case of login is failed***********")
            assert False


