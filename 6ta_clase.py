import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def load_page(url):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        has_element = driver.find_elements(By.XPATH, "//BUTTON[@autocomplete='off' and text()='Enable']")

        if has_element:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//BUTTON[@autocomplete='off' and text()='Enable']"))
            )
            element.click()

            print(f"Se hizo clic en el elemento 'Enable' en la página: {url}")

        print(f"Se accedio a la página: {url}")

    except Exception as e:
        print(f"Error al esperar el elemento en {url}: {e}")

        # Intento cargar la página de nuevo después de un corto período
        time.sleep(10)  # Espero 10 seg antes de intentar de nuevo
        print(f"Intentando cargar la página nuevamente: {url}")
        load_page(url)

    finally:
        time.sleep(8)
        driver.quit()

def run_colection(urls):
    for url in urls:
        load_page(url)

    # Después de recorrer todas las páginas, cargo la primera página de nuevo
    first_page = urls[0]
    load_page(first_page)

urls_to_navigate = [
    'https://www.example1.com',
    'https://www.example3.com',
    'https://the-internet.herokuapp.com/dynamic_controls'
]

run_colection(urls_to_navigate)
