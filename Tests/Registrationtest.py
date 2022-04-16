from selenium import webdriver
import time
import unittest
from Pages.basepage import Createpage



class CreateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_create1(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element_by_link_text("Sign in").click()

        create = Createpage(driver)
        create.enter_email("testuser1@shomit.com")
        create.click_create()

        # information
        create.enter_firstname("abc")
        create.enter_lastname("def")
        create.enter_password("12345")
        create.enter_address("123ab")
        create.enter_city("abc")
        create.select_state("1")
        create.enter_postcode("12345")
        create.enter_mobilephone("1234567890")
        create.click_submit()
        create.do_signout()

    def test_create2(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element_by_link_text("Sign in").click()

        create = Createpage(driver)
        create.enter_email("testuser2@shomit.com")
        create.click_create()

        # information
        create.enter_firstname("abc")
        create.enter_lastname("def")
        create.enter_password("12345")
        create.enter_address("123ab")
        create.enter_city("abc")
        create.select_state("1")
        create.enter_postcode("12345")
        create.enter_mobilephone("1234567890")
        create.click_submit()
        create.do_signout()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test OK")
