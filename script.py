#! /usr/bin/python3

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from notify import notification
import time
import datetime
import os
import argparse

# XPATH Selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INP_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_LBL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'
TARGET_NAME = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]'

# Targets
parser = argparse.ArgumentParser(description='WhatsApp Online Tracker')

parser.add_argument('-n', '--name',
                        dest='name',
                        required=True,
                    help='saved contact name of the target you wish to spy.\nExample: ./script.py -n "Your Boss Name"')

arg = parser.parse_args()

# Webdriver for Chrome 91
browser = webdriver.Chrome('./chromedriver')

# Load WhatsApp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

# Clear screen
os.system('clear')
print("Spying...")
run = True;
try: 
    while (run):

        tryAgain = True

        # Wait until new chat button is visible
        new_chat_btn = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        # Minimizing browser
        #browser.minimize_window()

        try:
            # Click new chat button
            new_chat_btn.click()

            # Wait until input field is visible
            inp_box = wait.until(EC.presence_of_element_located((By.XPATH, INP_BOX)))
            time.sleep(0.5)

            # Write phone number
            inp_box.send_keys(arg.name)
            
            time.sleep(1)

            # Press enter to confirm phone number
            inp_box.send_keys(Keys.ENTER)
        
            time.sleep(5)
            on = 1
            off = 1

            while(tryAgain): 
                now = datetime.datetime.now()
                trgt_name = browser.find_element_by_xpath(TARGET_NAME).get_attribute('innerText')
                try:
                    browser.find_element_by_xpath(ONLINE_LBL)
                    if(browser.find_element_by_xpath(ONLINE_LBL).get_attribute('innerText') == 'online'):
                        if(on == 1):
                            print(trgt_name + " is online at " + now.strftime("%Y-%m-%d %H:%M:%S"))
                            notification(trgt_name + " is online at " + now.strftime("%Y-%m-%d %H:%M:%S"), title="Whatsapp Spy") 
                            on = 0 
                            off = 1
                    #elif(browser.find_element_by_xpath(ONLINE_LBL).get_attribute('innerText') == 'typing...'):
                    #    print(trgt_name + " is typing at " + now.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        print("Don't mess around in the browser!")
                        tryAgain = False
                except: 
                    if(off == 1):
                        print(trgt_name + " is offline at " + now.strftime("%Y-%m-%d %H:%M:%S"))
                        notification(trgt_name + " is offline at " + now.strftime("%Y-%m-%d %H:%M:%S"), title="Whatsapp Spy")
                        on = 1
                        off = 0
                time.sleep(1)
                
        except:
            print("Something happened. Check if you are connected to WhatsApp Web.")
            browser.maximize_window()
except: 
    print('Uh-Oh! Catastrophic Failure, Bye.')
    run = False
    browser.quit()
