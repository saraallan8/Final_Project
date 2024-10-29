from pages.login import LogInPage
from selenium.webdriver.common.by import By

def test_login(browser):
        login_page = LogInPage(browser) 
        login_page.load()  
        login_page.login()
