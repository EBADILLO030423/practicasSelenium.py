from audioop import add
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)
addButton = driver.find_element(
    By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]")
driver.implicitly_wait(3)
plusButton = driver.find_element(
    By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]")
driver.implicitly_wait(3)
cartButton = driver.find_element(
    By.XPATH, "//header/div[1]/div[3]/a[4]/img[1]")
driver.implicitly_wait(3)
checkOutButton = driver.find_element(
    By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
driver.implicitly_wait(3)
plusButton.click()
addButton.click()
cartButton.click()
checkOutButton.click()
driver.quit()
