import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def completeForm():
    name = "Alejandro Oscar"
    surname = "Arrua"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/path/to/chromium'

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://validaciones.rodrigovillanueva.com.mx/index.html")
    driver.maximize_window()

    inputName = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/form[1]/div[1]/input[1]")
    inputName.send_keys(name)

    inputSurname = driver.find_element(By.XPATH, "//input[contains(@id,'apellidos')]")
    inputSurname.send_keys(surname)
    time.sleep(60)

    driver.close()

completeForm()
