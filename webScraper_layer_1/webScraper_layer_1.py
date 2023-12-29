from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os



PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"

url = "https://www.foodandwine.com/appetizers/meze/mediterranean"


service = Service(executable_path= PATH)

driver = webdriver.Chrome(service=service)

driver.get(url)

input_element = driver.find_element(By.CLASS_NAME, "comp list-sc-item mntl-block mntl-sc-list-item")

print(input_element)