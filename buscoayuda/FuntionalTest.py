import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class FunctionalTest(TestCase):
    def setUp(self):
        sistemaop = sys.platform
        print('so ' + sistemaop)
        if sistemaop == 'linux':
            self.browser = webdriver.Chrome()
        elif sistemaop == 'win32':
            self.browser = webdriver.Chrome('C://chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://localhost:8000')
        print(self.browser.title)
        self.assertIn('Busco ayuda', self.browser.title)