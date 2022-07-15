# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

# driver = webdriver.Chrome()
driver = uc.Chrome(use_subprocess=True)

driver.get(
    "https://accounts.google.com/ServiceLogin/identifier?service=youtube&uilel=3&passive=true&continue=https%3A"
    "%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A"
    "%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

phone = "xxx"
password = "xxx"


def login_test():
    element = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    element.send_keys(phone)
    time.sleep(10)
    element.send_keys(Keys.RETURN)
    time.sleep(10)
    element = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    time.sleep(15)  # waiting 3 minutes after executed login form submission
    driver.close()  # chrome will be automatically closed after 3 minutes


if _name_ == '_main_':
    login_test()
