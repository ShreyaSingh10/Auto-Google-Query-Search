import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():

    #we are initialising Chrome by making an object of it
    driver = webdriver.Chrome(executable_path= r'.\\driver\\chromedriver.exe')
    
    #wait for 5 seconds for page to open
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query):
    #will get the google page
    driver.get("http://www.google.com")
    try:

        #finding by name the of the input box
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))

        #finding by name of the input button
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))

        #will send our query or type it into the input box
        box.send_keys(query)

        #We trigger submit event on button object because in html input for button the type=submit we can use click aswell
        button.submit()
    except TimeoutException:
        #just in case if the input box are button did not load we will get an error in searching
        print("Box or Button not found in google.com")
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Automating Tasks With Python")

    #wait for 15 seconds before closeing the browser
    time.sleep(15)

    #closing the browser after 15seconds
    driver.quit()