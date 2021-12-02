from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")




# url of home page
url =  "http://127.0.0.1:8000/"
# url2 = "http://127.0.0.1:8000/accounts/login/" :- url of login page

driver.get(url)

time.sleep(3)
driver.find_element_by_id('signin').click()

time.sleep(3)
# move to login page


username = "aditya"
password = "aditya33"



driver.find_element_by_name("username").send_keys(username)

time.sleep(2)
driver.find_element_by_name("password").send_keys(password)
time.sleep(2)

driver.find_element_by_css_selector('[type=submit]:not(:disabled), button:not(:disabled)').click()



time.sleep(2)
# move to the user dashboard after login

# scroll the webpage

y = 100
for timer in range(0,8):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 150
    time.sleep(1)


driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(2)

# head to sign out page
driver.find_element_by_id("signout").click()

time.sleep(3)

# logout from the account
 
driver.find_element_by_id("logout").click()

time.sleep(2)

driver.close()