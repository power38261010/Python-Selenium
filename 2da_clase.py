from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def autoLogin():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/path/to/chromium'
    chrome_options.add_argument('--headless')
    username_git = "power38261010"
    password_git = "camilo94"

    browser = webdriver.Chrome(options=chrome_options)

    browser.get("https://github.com/login")
    # browser.maximize_window()

    username = browser.find_element(By.XPATH, "//input[@name='login']")
    password = browser.find_element(By.XPATH, "//input[@name='password']")
    submit = browser.find_element(By.XPATH, "//input[@name='commit']")

    username.send_keys(username_git)
    password.send_keys(password_git)

    submit.click()

    wait = WebDriverWait(browser, 10)
    current_title = browser.title
    print("Título actual de la página:", current_title)

    wait.until(EC.title_contains("GitHub"))

    # profile_link = browser.find_element(By.XPATH, "//a[contains(text(),'Your profile')]")
    # profile_link.click()
    # time.sleep(60)
    browser.quit()
autoLogin()

