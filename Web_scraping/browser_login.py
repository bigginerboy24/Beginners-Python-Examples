from selenium import webdriver
import time

# You can change Firefox to Safari and Chrome too
driver = webdriver.Firefox()
website = driver.get("https://www.website.com/")

# Input "email" and "pass" here change based on websites page source
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

#button = driver.find_element_by_class_name("btn"), this for github and reddit

button = driver.find_element_by_id('loginbutton')

time.sleep(0.5)
# Write your email and password
username.send_keys("your@email.com")
password.send_keys("password")

time.sleep(0.3)

button.click()

time.sleep(60)
