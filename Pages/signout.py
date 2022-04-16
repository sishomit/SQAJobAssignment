from Locators.locators import Locators


class Signout():

    def __init__(self, driver):
        self.driver = driver

        self.signout_button = Locators.signout_button_name

    def click_signout(self):
        self.driver.find_element_by_id(self.signout_button).click()
