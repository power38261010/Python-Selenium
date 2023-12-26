import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def completeForm ():
    name="Alejandro"
    surname="Arrua"
    driver=webdriver.Chrome()
    driver.get("https://validaciones.rodrigovillanueva.com.mx/index.html")
    driver.maximize_window()

    inputName=driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/form[1]/div[1]/input[1]")
    inputName.send_keys(name+" "+surname)
    time.sleep(5)

    driver.close()

completeForm()