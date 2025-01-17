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

class Test2AsignarRolEmpleado():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_2AsignarRolEmpleado(self):
    self.driver.get("http://localhost:64927/")
    self.driver.set_window_size(1920, 1032)
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Mantenedor").click()
    self.driver.find_element(By.LINK_TEXT, "Usuarios").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "txtNombres").click()
    self.driver.find_element(By.ID, "txtNombres").send_keys("Selenium")
    self.driver.find_element(By.ID, "txtApellidos").send_keys("Test")
    self.driver.find_element(By.ID, "txtCorreo").send_keys("selenium@gmail.com")
    self.driver.find_element(By.ID, "txtClave").send_keys("789")
    self.driver.find_element(By.ID, "cboRol").click()
    dropdown = self.driver.find_element(By.ID, "cboRol")
    dropdown.find_element(By.XPATH, "//option[. = 'EMPLEADO']").click()
    self.driver.find_element(By.ID, "btnGuardarCambios").click()
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > .sorting_1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > .sorting_1").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > .sorting_1").text == "EMPLEADO"
    self.driver.find_element(By.CSS_SELECTOR, "strong").click()
  
