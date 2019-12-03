import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Blog_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_enroll(self):
        user = "mattharris"
        pwd = "admin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/student_home")
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p/a").click()
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div[2]/a").click()

        try:
            elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[2]/div[2]/a")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
