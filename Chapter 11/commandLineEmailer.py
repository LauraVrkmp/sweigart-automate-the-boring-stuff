from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, sys

def loginHotmail():
    hotmailId = sys.argv[1]
    passWord = sys.argv[2]
    email = sys.argv[3]
    topic = sys.argv[4]
    message = sys.argv[5]

    driver = webdriver.Firefox()
    driver.get('https://hotmail.com')
    time.sleep(5)

    loginButton = driver.find_elements(By.ID, 'mectrl_headerPicture')
    loginButton[0].click()

    time.sleep(8)
    loginBox = driver.find_element(By.ID, 'i0116')
    loginBox.send_keys(hotmailId)
    time.sleep(2)
    nextButton = driver.find_elements(By.ID, 'idSIButton9')
    nextButton[0].click()
    time.sleep(4)

    passWordBox = driver.find_element(By.ID, 'i0118')
    passWordBox.send_keys(passWord)
    time.sleep(2)
    signInButton = driver.find_elements(By.ID, 'idSIButton9')
    signInButton[0].click()
    time.sleep(4)
    acceptButton = driver.find_elements(By.ID, 'acceptButton')
    acceptButton[0].click()
    time.sleep(12)

    newMail = driver.find_elements(By.ID, 'id__25')
    newMail[0].click()
    time.sleep(8)

    addressedTo = driver.find_elements(By.CLASS_NAME, '___1mtnehv')
    addressedTo[0].send_keys(email)
    time.sleep(2)
    # topicField = driver.find_elements(By.CLASS_NAME, 'ms-TextField-field')
    # topicField[0].send_keys(topic)
    # # time.sleep(2)
    # messageField = driver.find_element(By.CLASS_NAME, 'dFCbN')
    # messageField[0].send_keys(message)
    # time.sleep(2)

    # 
    # add code to send email


loginHotmail()