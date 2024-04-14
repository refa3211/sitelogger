# import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
load_dotenv() 


username = os.getenv('USER')
password = os.getenv('PASS')
print(username, password)


def login():
    
    driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
    driver.get("https://vpn5.health.gov.il")
    time.sleep(3)

    email_input = driver.find_element(By.ID, "input_1")
    email_input.send_keys(username)
    time.sleep(3)
    password_input = driver.find_element(By.ID, "input_2")
    password_input.send_keys(password)
    time.sleep(1)
    dropdown = Select(driver.find_element(By.ID, "input_3"))  # Replace "dropdown_id" with the actual ID of the dropdown
    dropdown.select_by_visible_text("Google_Authenticator")
    # password_input.send_keys(Keys.RETURN)

    time.sleep(5) 
    
  
    # driver.quit()


if __name__ == "__main__":
    login()