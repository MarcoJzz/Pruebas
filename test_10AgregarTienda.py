# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test10AgregarTienda():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_10AgregarTienda(self):
    self.driver.get("http://localhost:64927/")
    self.driver.set_window_size(1920, 1032)
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Ventas").click()
    self.driver.find_element(By.LINK_TEXT, "Tiendas").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtNombre").click()
    self.driver.find_element(By.ID, "txtNombre").send_keys("Tienda 002")
    self.driver.find_element(By.ID, "txtRuc").click()
    self.driver.find_element(By.ID, "txtRuc").send_keys("21314345213")
    self.driver.find_element(By.ID, "txtDireccion").click()
    self.driver.find_element(By.ID, "txtDireccion").send_keys("av. mangos")
    self.driver.find_element(By.ID, "txtTelefono").click()
    self.driver.find_element(By.ID, "txtTelefono").send_keys("8093630923")
    self.driver.find_element(By.ID, "btnGuardarCambios").click()
    self.driver.find_element(By.CSS_SELECTOR, ".even .btn-danger").click()
    self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
    self.driver.find_element(By.CSS_SELECTOR, "strong").click()
  
