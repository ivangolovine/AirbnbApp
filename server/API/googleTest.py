from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import selenium
import json
import re
import sys
import time
import os
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()

# No need to specify binary_location when using GeckoDriver
# options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Comment out or remove this line
options.ignore_local_proxy_environment_variables()


loggedIn = False
cookies = ""


def createDictEnv():
    dictLogin = {}
    
    load_dotenv(dotenv_path="secrets/.env")
    dictLogin["userName"] = os.getenv('EMAIL')
    dictLogin["password"]  = os.getenv('PASSWORD')
    return dictLogin


def login_Airbnb():
    dictLogin = createDictEnv()
    
    # Opens the browser
    driver = webdriver.Firefox(options=options)  # Auto use GeckoDriver
    driver.get("https://www.airbnb.ca/login")
    
    
    #set view size
    driver.set_window_size(1000, 1400)
    
    #dismiss the cookie popup
    continue_email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".b3lti07.atm_gi_1pzushe.atm_gi_idpfg4__oggzyc.atm_vv_1q9ccgz__oggzyc.ad6rpx.atm_jb_jijo1b.iv91188.atm_h0_i2wt44__oggzyc.atm_gz_i2wt44__qky54b")))
    continue_email_field.click()
    
    
    #Targets the email login field
    time.sleep(4)
    continue_email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Continue with email']")))
    # Click on the email login field
    continue_email_field.click()

    
    # Sends Email to the login
    driver.find_element("id", "email-login-email").send_keys(dictLogin.get("userName"))

    continue_emai_login = driver.find_element(By.CSS_SELECTOR, "[data-testid='signup-login-submit-btn']")
    continue_emai_login.click()

    # Sends Password to the login
    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email-signup-password")))
    password_input.send_keys(dictLogin.get("password"))
    #driver.find_element("id", "email-signup-password").send_keys(dictLogin.get("password"))
    
    time.sleep(4)
    
    continue_final_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='signup-login-submit-btn']")))
    continue_final_login.click()




'''
def login_Airbnb_bs4():
    dictLogin = createDictEnv()
    
    if not loggedIn:
        s = requests.Session()
        src = s.get('https://www.airbnb.com/login').text
        soup = BeautifulSoup(src, features="html.parser")
        hidden_tags = soup.findAll("input")
        
        #userNameTag = soup.find("input")
        
        payload = {
            'email': dictLogin.get('userName'),
        }
        
        for tag in hidden_tags:
           payload[tag.attrs['name']] = tag.attrs['value']
           

        print(payload)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',  # Add your user-agent here
            'Referer': 'https://www.airbnb.com/login',  # Add Referer header if required
            # Add any other headers required by the website
        }

        response = s.post('https://www.airbnb.com/login', data=payload, headers=headers)


        status = response.headers.get('status')
        
        # Print response status code
        print("Response status code:", status)
        
        # Print response headers
        #print("Response headers:", response.headers)
        #print("Response Content: {}".format(response.text))
        # Now you can inspect the response to check if login was successful
        if response.status_code in [200, 302]:
            print("Login successful")
            # Continue with your logic after successful login
        else:
            print("Login failed")
            
            
        #print(payload)
        #response_Airbnb = s.post('https://www.airbnb.com/authenticate', data=payload)
        
        
        
        payload2 = {
            'password': dictLogin.get('password')
        }
        if response_Airbnb.status_code in [200, 302]:
            cookies = s.cookies
            #loggedIn = True
            print("Logged In succefully")
        else:
            print("Login Failed")

def terminal_prompt():
    while True:
        print("Press 'q' to quit")
        command = input().strip().lower()
        if command == 'q':
            print("Exiting the program.")
            break
        elif command == "l":
            login_Airbnb()
        else:
            print("Invalid command. Press 'q' to quit.")

'''