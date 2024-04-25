import time
from selenium import webdriver
from selenium.webdriver.common.by import By

BRAVE_PATH = r"C:\\Users\\Refael\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
CHROMEDRIVER_PATH = r"C:\\Users\\Refael\\Documents\\Github\\sitelogger\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH
service = webdriver.ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(options=options, service=service)


driver.get("https://google.com")
time.sleep(5)
