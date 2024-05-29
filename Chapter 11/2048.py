from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def playGame():
    driver = webdriver.Firefox()
    driver.get('https://gabrielecirulli.github.io/2048/')

    time.sleep(5)
    accept_button = driver.find_element(By.XPATH, '//button[text()="Continue with Recommended Cookies"]')
    accept_button.click()
    time.sleep(5)

    html_elem = driver.find_element(By.TAG_NAME, 'html')

    while True:
        html_elem.send_keys(Keys.UP)
        time.sleep(1)
        html_elem.send_keys(Keys.RIGHT)
        time.sleep(1)
        html_elem.send_keys(Keys.DOWN)
        time.sleep(1)
        html_elem.send_keys(Keys.LEFT)
        time.sleep(1)

playGame()
