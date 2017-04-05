'''
Python script to automate the Goodlife membership in order to earn
quaterly 1000 points in virginpulse

Note: Make sure you have dummyPDF.pdf file in the same directory as
this python script in order to execute

Please follow requirements.txt file to know what to install

To format file:
Install
sudo  pip install --upgrade autopep8

Run:
autopep8 --in-place --aggressive --aggressive  <filename>
'''

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import os


driver = webdriver.Chrome()

''' for windows
driver = webdriver.Chrome("C:\Users\eripflo\AppData\Local\Temp\Rar$EXa0.403\chromedriver.exe")
'''

driver.get("https://survey.virginpulse.com/ericsson-gym-membership")

driver.find_element_by_id('oUserID').send_keys(
    'User Email' + Keys.TAB)
driver.find_element_by_id('oPwdID').send_keys('Enter Password')
time.sleep(1)
driver.find_element_by_id('oLogon').click()

time.sleep(5)

driver.find_element_by_xpath("//*[@id=\"emailAddress\"]").send_keys(
    'dummyemail@hotmail.com' +
    Keys.TAB +
    Keys.TAB +
    Keys.TAB +
    Keys.TAB +
    "GOODlIFE" +
    Keys.TAB +
    "GoodLife Fitness")

# Make sure pdf file is in the same directory and with same name
driver.find_element_by_id("fileToUpload").send_keys(
    os.getcwd() + "/dummyPDF.pdf")

time.sleep(2)

# Submit the form
driver.find_element_by_id("submitButton").click()
