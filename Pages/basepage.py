from selenium.webdriver.support.select import Select

from Locators.locators import Locators


class Createpage():

    def __init__(self, driver):
        self.driver = driver
        #Create account
        self.email_textbox_id = Locators.email_textbox_id
        self.create_button_name = Locators.create_button_name

        #Account information
        self.first_name = Locators.firstname_id
        self.last_name = Locators.lastname_id
        self.set_password = Locators.password_id
        self.set_address = Locators.address
        self.set_city = Locators.city_id
        self.set_state = Locators.state_id
        self.set_postcode = Locators.postcode_id
        self.set_mobile = Locators.mobile
        self.submit_button_id = Locators.submit_buttoon_id

        #signout
        self.signingout = Locators.signout_class

    # Create account
    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def click_create(self):
        self.driver.find_element_by_id(self.create_button_name).click()

    # informtaion
    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.first_name).clear()
        self.driver.find_element_by_id(self.first_name).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.last_name).clear()
        self.driver.find_element_by_id(self.last_name).send_keys(lastname)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.set_password).clear()
        self.driver.find_element_by_name(self.set_password).send_keys(password)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.set_address).clear()
        self.driver.find_element_by_id(self.set_address).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.set_city).clear()
        self.driver.find_element_by_id(self.set_city).send_keys(city)

    def select_state(self, value):
        statemark = self.driver.find_element_by_id(self.set_state)
        statechoose = Select(statemark)
        statechoose.select_by_value(value)

    def enter_postcode(self, postcode):
        self.driver.find_element_by_id(self.set_postcode).clear()
        self.driver.find_element_by_id(self.set_postcode).send_keys(postcode)

    def enter_mobilephone(self, mobilephone):
        self.driver.find_element_by_id(self.set_mobile).clear()
        self.driver.find_element_by_id(self.set_mobile).send_keys(mobilephone)

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()

    # signout
    def do_signout(self):
        self.driver.find_element_by_xpath(self.signingout).click()
