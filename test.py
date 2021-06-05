from selenium import webdriver

browser = webdriver.Chrome(r'./chromedriver')
browser.get('https://github.com')

browser.quit()
