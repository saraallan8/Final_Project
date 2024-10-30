from selenium.webdriver.common.by import By
import time
class Purchase:       
#Locators
  add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
  cart_icon = (By.CLASS_NAME, "shopping_cart_link")
  checkout_button = (By.ID, "checkout")
  firstname_field = (By.ID, "first-name")
  lastname_field = (By.ID, "last-name")
  postalcode_field = (By.ID, "postal-code")
  continue_button = (By.ID, "continue")
  finish_button = (By.ID, "finish")
  backhome_button = (By.ID, "back-to-products")

#Initializer
  def __init__(self,browser):
    self.browser = browser

#Interaction Method
  def purchase(self):
   add_to_cart = self.browser.find_element(*self.add_to_cart_button)
   add_to_cart.click()
   time.sleep(3)
   cart = self.browser.find_element(*self.cart_icon)
   cart.click()
   time.sleep(3)
   checkout = self.browser.find_element(*self.checkout_button)
   checkout.click()   
   time.sleep(3)
   firstname = self.browser.find_element(*self.firstname_field)     
   firstname.send_keys("Sara")
   time.sleep(3)
   lastname = self.browser.find_element(*self.lastname_field)
   lastname.send_keys("Allan")
   time.sleep(3)
   postalcode = self.browser.find_element(*self.postalcode_field)
   postalcode.send_keys("P720")
   time.sleep(3)
   continueb = self.browser.find_element(*self.continue_button)
   continueb.click()
   time.sleep(3)
   finish = self.browser.find_element(*self.finish_button)
   finish.click()
   time.sleep(3)
   backhome = self.browser.find_element(*self.backhome_button)
   backhome.click()
   time.sleep(3)
