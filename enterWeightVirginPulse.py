from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://app.member.virginpulse.com/#/healthyhabits?tracker=1")

driver.find_element_by_id('oUserID').send_keys(
    'Enter UserName' + Keys.TAB)
driver.find_element_by_id('oPwdID').send_keys('EnterPassword')
time.sleep(1)
driver.find_element_by_id('oLogon').click()

time.sleep(5)


driver.find_element_by_xpath("//*[@id=\"healthyhabits-weightinput\"]").send_keys(Keys.DELETE+"150"+Keys.TAB+Keys.ENTER)