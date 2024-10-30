from pages.login import LogInPage
from pages.purchase import Purchase


def test_purchase(browser):
 loginpage = LogInPage(browser)
 purchase_page = Purchase(browser)
 loginpage.load()
 loginpage.login()
 purchase_page.purchase()