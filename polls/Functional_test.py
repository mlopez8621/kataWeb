import random
import sys

import os

__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome("C:\\Users\\CarriCas\\Documents\\Platzi\\Django\\comple\\chromedriver_win32\\chromedriver.exe")
        self.browser = webdriver.Chrome(executable_path=r"files/chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('BuscoAyuda', self.browser.title)


    def test_2_registro(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Andres Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        ruta= os.path.join(sys.path[0], "polls/files", 'desarrollo.jpg')

        if os.name == 'nt':
            ruta = ruta.replace("\\","/")
            imagen.send_keys(ruta)
        else:
            imagen.send_keys(ruta)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('janiel645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="Andres Daniel Arevalo"]')

        self.assertIn('Andres Daniel Arevalo', span.text)

    def test_3_detail(self):
        self.browser.get('http://127.0.0.1:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_4_login(self):
        self.browser.get('http://127.0.0.1:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        self.browser.implicitly_wait(1)

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('daniel645')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('clave123')

        btnLogin = self.browser.find_element_by_id('btnLogin')
        btnLogin.click()

        a= self.browser.find_element(By.XPATH, '//a[text()="daniel645"]')
        self.assertIn('daniel645', a.text)

