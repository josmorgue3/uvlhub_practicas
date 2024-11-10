import pytest
import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configurar Selenium para usar Chromium
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Usar webdriver-manager para gestionar el driver de Chromium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://localhost:5000/login")
time.sleep(2)
driver.set_window_size(912, 1011)
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("user1@example.com")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "submit").click()
time.sleep(2)
driver.get("http://localhost:5000/notepad/create")
time.sleep(2)
driver.find_element(By.ID, "title").click()
driver.find_element(By.ID, "title").send_keys("n1")
driver.find_element(By.ID, "body").click()
driver.find_element(By.ID, "body").send_keys("n1")
driver.find_element(By.ID, "submit").click()