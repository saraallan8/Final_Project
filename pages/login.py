from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LogInPage:
#Locators
  username_field = (By.ID, "user-name")
  password_field = (By.ID, "password")
  login_button = (By.ID, "login-button")

#Initializer
  def __init__(self, browser):
   self.browser = browser 

#Interaction Method
  def load(self): 
    URL = "https://www.saucedemo.com/"
    self.browser.get(URL) 

  def login(self):
   username = self.browser.find_element(*self.username_field)
   username.send_keys("standard_user")
   password = self.browser.find_element(*self.password_field)
   password.send_keys("secret_sauce")
   loginb = self.browser.find_element(*self.login_button)
   loginb.click()
   time.sleep(3)
