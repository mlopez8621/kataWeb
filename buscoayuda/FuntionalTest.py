import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('C//chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://www.google.com.co')
        self.assertIn('Google', self.browser.title)