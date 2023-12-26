from abc import ABC, abstractmethod
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timer


# Creo una superclase cuyo metodos son abstractos y sus hijos los cuales van a actuar diferente segun la dinamica de los hijos

class AbstractLogin(ABC):
    credentials = None

    def __init__(self, ruta_ods):
        self.credentials = self.obtener_credenciales_desde_excel(ruta_ods)

    @abstractmethod
    def obtener_credenciales_desde_excel(self, ruta_ods):
        pass

    @abstractmethod
    def auto_login(self):
        pass

class GitHubLogin(AbstractLogin):
    def obtener_credenciales_desde_excel(self, ruta_ods):
        try:
            df = pd.read_excel(ruta_ods, engine='odf', header=None)

            username = df.iloc[0, 0]
            password = df.iloc[0, 1]
            url = df.iloc[0, 2]

            return {
                "username_github": username,
                "password_github": password,
                "url_github": url
            }

        except Exception as e:
            print("Error al obtener credenciales desde ODF (plantilla de cálculo):", e)
            return None

    def auto_login(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')

            browser = webdriver.Chrome(options=chrome_options)

            if not self.credentials.get("sesion_iniciada", False):
                browser.get(self.credentials["url_github"])

                username_input = browser.find_element(By.XPATH, "//input[@name='login']")
                password_input = browser.find_element(By.XPATH, "//input[@name='password']")
                submit_button = browser.find_element(By.XPATH, "//input[@name='commit']")

                username_input.send_keys(self.credentials["username_github"])
                password_input.send_keys(self.credentials["password_github"])

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


# Usando instancia de la clase autologin

ruta_excel = "/home/alejandro/Escritorio/prueba.ods"
github_login_instance = GitHubLogin(ruta_excel)

github_login_instance.auto_login()
