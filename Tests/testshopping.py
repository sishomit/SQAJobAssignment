from selenium import webdriver
import time
import unittest
from Pages.shopping import Shopping


class ShoppingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(
            executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_create(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.find_element_by_link_text("Sign in").click()
        emails = ["testuser1@shomit.com", "testuser2@shomit.com"]
        for x in emails:
            login = Shopping(driver)
            login.enter_email(x)
            login.enter_password("12345")
            login.click_login()

            login.click_tshirt()
            login.do_filter()
            login.go_product()
            login.add_cart()
            login.checkout()
            login.checkout2()
            login.checkout3()
            login.checkmark()
            login.ship()
            login.pay()
            login.do_confirm()
            login.signout()
            time.sleep(5)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test OK")
