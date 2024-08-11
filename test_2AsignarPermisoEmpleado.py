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

class Test1AsignarPermisoEmpleado():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1AsignarPermisoEmpleado(self):
    self.driver.get("http://localhost:64927/")
    self.driver.set_window_size(1920, 1032)
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Mantenedor").click()
    self.driver.find_element(By.LINK_TEXT, "Asignar Permisos").click()
    self.driver.find_element(By.ID, "cboRol").click()
    dropdown = self.driver.find_element(By.ID, "cboRol")
    dropdown.find_element(By.XPATH, "//option[. = 'EMPLEADO']").click()
    self.driver.find_element(By.ID, "btnBuscar").click()
    element = self.driver.find_element(By.ID, "btnBuscar")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) input").click()
    self.driver.find_element(By.ID, "btnGuardarCambios").click()
    self.driver.find_element(By.CSS_SELECTOR, "strong").click()
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.CSS_SELECTOR, ".justify-content-center").click()
    self.driver.find_element(By.NAME, "correo").send_keys("tienda@gmail.com")
    self.driver.find_element(By.NAME, "clave").send_keys("456")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Mantenedor").click()
    self.driver.find_element(By.LINK_TEXT, "Usuarios").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn-success")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "strong").click()
  