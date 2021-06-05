from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
import os

# XPATH Selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INP_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_LBL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'

# Targets #TODO

# Webdriver for Chrome 91
browser = webdriver.Chrome('./chromedriver')

# Load WhatsApp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    # Clear screen
    os.system('clear')

    tryAgain = True

    # Wait until new chat button is visible
    new_chat_btn = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

    while (tryAgain):
        try:
            # Click new chat button
            new_chat_btn.click()

            # Wait until input field is visible
            inp_box = wait.until(EC.presence_of_element_located((By.XPATH, INP_BOX)))
            time.sleep(0.5)

            # Write phone number
            inp_box.send_keys('9625944410')  #TODO 
            
            time.sleep(1)

            # Press enter to confirm phone number
            inp_box.send_keys(Keys.ENTER)

            time.sleep(5)
            tryAgain = False

            try:
                try: 
                    browser.find_element_by_xpath(ONLINE_LBL)
                    print(' is online')
                except:
                    print(' is offline')
                    time.sleep(1)
            except:
                print('Exception 1')
                time.sleep(10)
        except:
            print('Exception 2')
            time.sleep(4)

