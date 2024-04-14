# import requests
import os
from platform import python_branch
import re
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import pyotp
import time
load_dotenv() 


username = os.getenv('USER')
password = os.getenv('PASS')
OTPCODE = os.getenv('OTPSECERT')


def otpcode():
    totp = pyotp.TOTP(OTPCODE)
    print(totp.now())
    return totp.now()



def login():
    
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://vpn5.health.gov.il")
    time.sleep(2)

    #username
    email_input = driver.find_element(By.ID, "input_1")
    email_input.send_keys(username)
    time.sleep(1.5)
    #password
    password_input = driver.find_element(By.ID, "input_2")
    password_input.send_keys(password)
    time.sleep(1.5)
    #select auth method 
    dropdown = Select(driver.find_element(By.ID, "input_3"))  # Replace "dropdown_id" with the actual ID of the dropdown
    dropdown.select_by_visible_text("Google_Authenticator")
    password_input.send_keys(Keys.RETURN)
    time.sleep(1.5)

    #page 2 enter otp code
    otpinput = driver.find_element(By.ID, "input_1")
    otpinput.send_keys(otpcode())
    time.sleep(1)
    password_input.send_keys(Keys.RETURN)

    time.sleep(20) 
    
  
    # driver.quit()


if __name__ == "__main__":
    login()
    otpcode()