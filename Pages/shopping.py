from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Locators.locators import Locators



class Shopping():

    def __init__(self, driver):
        self.driver = driver

        self.loginemail_textbox_id = Locators.login_email_textbox_id
        self.loginpassword_textbox_id = Locators.login_password_textbox_id
        self.login_button = Locators.login_button_id

        self.go_to_tshirt = Locators.go_to_tshirt_link

        self.filter = Locators.filter_button_id
        self.goto_product = Locators.product_link_text

        self.cartadd = Locators.add_to_cart_button

        self.checkingout = Locators.checkout_button_class
        self.checkingout_confirm = Locators.confirm_Checkout_class
        self.checkingout_confrim_next = Locators.confirm_Checkout_next
        self.checkbox = Locators.checkerbox
        self.shipping = Locators.confirm_shipping
        self.payment = Locators.payment_class
        self.confiramtion = Locators.confirmation_class
        self.signingout = Locators.signout_class

    def enter_email(self, email):
        self.driver.find_element_by_id(self.loginemail_textbox_id).clear()
        self.driver.find_element_by_id(self.loginemail_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.loginpassword_textbox_id).clear()
        self.driver.find_element_by_id(self.loginpassword_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button).click()

    def click_tshirt(self):
        self.driver.get(self.go_to_tshirt)

    def do_filter(self):
        self.driver.find_element_by_id(self.filter).click()

    def go_product(self):
        self.driver.find_element_by_link_text(self.goto_product).click()

    def add_cart(self):
        self.driver.find_element_by_name(self.cartadd).click()

    def checkout(self):
        self.driver.find_element_by_xpath(self.checkingout).click()

    def checkout2(self):
        self.driver.find_element_by_xpath(self.checkingout_confirm).click()

    def checkout3(self):
        self.driver.find_element_by_name(self.checkingout_confrim_next).click()

    def checkmark(self):
        self.driver.find_element_by_xpath(self.checkbox).click()

    def ship(self):
        self.driver.find_element_by_name(self.shipping).click()

    def pay(self):
        self.driver.find_element_by_xpath(self.payment).click()

    def do_confirm(self):
        self.driver.find_element_by_xpath(self.confiramtion).click()

    def signout(self):
        self.driver.find_element_by_xpath(self.signingout).click()

