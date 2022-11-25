from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://courses.letskodeit.com/practice")
bmwRadioButton = driver.find_element(By.ID, "bmwradio")
benzRadioButton = driver.find_element(By.ID, "benzradio")
hondaRadioButton = driver.find_element(By.ID, "hondaradio")

bmwRadioButton.click()
benzRadioButton.click()
hondaRadioButton.click()


driver.implicitly_wait(3)
