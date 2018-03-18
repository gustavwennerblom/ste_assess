import unittest
import random
from flask_testing import LiveServerTestCase
from selenium import webdriver
from main import app
import time
from config import UnitTestConfig


# noinspection PyAttributeOutsideInit
class TestUI(LiveServerTestCase):
    def create_app(self):
        app.config.from_object(UnitTestConfig)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_root_access(self):
        """
        Test that Selenium can access the start page
        """
        self.driver.get(self.get_server_url())
        self.assertIn("Steps to Export", self.driver.title)

    def test_submit_assessment(self):
        """
        Set up for visual inspection of result page from a random survey submission
        :return: Nothing
        """
        self.driver.get(self.get_server_url())
        for i in range(1, 26):
            option_no = random.randint(0, 2)
            target_id = "q" + str(i) + "-" + str(option_no)
            input_control_label = self.driver.find_element_by_css_selector('label[for={}'.format(target_id))
            input_control_label.click()
            # input_control = self.driver.find_element_by_id(target_id)
            # input_control.click()
        submit_control = self.driver.find_element_by_id("submit")
        submit_control.click()
        input('Press ENTER after visual inspection')
        self.driver.get(self.get_server_url())
        flashed_message = self.driver.find_element_by_class_name("flashes")
        self.assertIn('svarat tidigare', flashed_message.text)
        input("Press ENTER to finalize test sequence")

    def __test_z_cookie_is_set(self):
        # NOT YET WORKING
        from werkzeug.http import parse_cookie
        # response = self.client.get('/', follow_redirects=True)
        self.driver.get(self.get_server_url())
        flashed_message = self.driver.find_element_by_class_name("flashes")
        self.assertIn('svarat tidigare', flashed_message.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
