import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_credenciales_desde_excel():
    try:
        ruta_ods = "/home/alejandro/Escritorio/prueba.ods"

        df = pd.read_excel(ruta_ods, engine='odf', header=None)

        username = df.iloc[0, 0]
        password = df.iloc[0, 1]
        url = df.iloc[0, 2]

        credentials_github = {
            "username_github": username,
            "password_github": password,
            "url_github": url
        }

        return credentials_github

    except Exception as e:
        print("Error al obtener credenciales desde ODF (plantilla de cálculo):", e)
        return None

def auto_login(credentials):
    try:
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')

        browser = webdriver.Chrome(options=chrome_options)

        if not credentials.get("sesion_iniciada", False):
            browser.get(credentials["url_github"])

            username_input = browser.find_element(By.XPATH, "//input[@name='login']")
            password_input = browser.find_element(By.XPATH, "//input[@name='password']")
            submit_button = browser.find_element(By.XPATH, "//input[@name='commit']")

            username_input.send_keys(credentials["username_github"])
            password_input.send_keys(credentials["password_github"])

            submit_button.click()

            wait = WebDriverWait(browser, 10)
            current_title = browser.title
            print("Título actual de la página:", current_title)

            wait.until(EC.title_contains("GitHub"))

            time.sleep(4)
            browser.quit()

    except Exception as un_error:
        print("Ocurrió un error de tipo:", type(un_error))
        print("Detalles del error:", un_error)

credentials = obtener_credenciales_desde_excel()

if credentials:
    try:
        auto_login(credentials)
    except Exception as un_error:
        print("Ocurrió un error de tipo:", type(un_error))
else:
    print("No se pudieron obtener las credenciales desde Excel.")
