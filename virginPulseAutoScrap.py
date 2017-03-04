from selenium.webdriver.common.keys import Keys 
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
import time
from selenium.webdriver import ActionChains

#Install pip: http://stackoverflow.com/questions/4750806/how-do-i-install-pip-on-windows 
#Install selenium via http://selenium-python.readthedocs.io/installation.html (pip install selenium) 
#Please install Chrome driver via https://chromedriver.storage.googleapis.com/index.html?path=2.27/ 
#Webdriver Documentation: http://selenium-python.readthedocs.io/locating-elements.html 


driver = webdriver.Chrome()

''' for windows
driver = webdriver.Chrome("C:\Users\eripflo\AppData\Local\Temp\Rar$EXa0.403\chromedriver.exe")
'''
driver.get("https://member.virginpulse.com/login.aspx")
 
driver.find_element_by_id('oUserID').send_keys('user'+Keys.TAB) 
driver.find_element_by_id('oPwdID').send_keys('pass')
time.sleep(1) 
driver.find_element_by_id('oLogon').click()

'''
 After login success, there is usually highlights such as trophy for steps, challenges, etc. Action
 performed here is closing that
'''
try: 
    driver.find_element_by_class_name('close-trophy-popup-wrapper').click() 
except NoSuchElementException: 
    print("No such thing")

time.sleep(5)

'''
 Here we are trying to click both the daily cards
'''
try:
	driver.find_element_by_id('triggerCloseCurtain').click()
	time.sleep(2)
	for i in range(1,3):
		driver.find_element_by_xpath("//*[@id=\"daily-tips-slider\"]/div[%d]/daily-cards/div/div[3]/div[6]/img[1]" % i)
	driver.find_element_by_id('triggerCloseCurtain').click()
except NoSuchElementException:
	print("No cards to check")


time.sleep(2)

'''
We are going to click below to view the Healthy Daily Habits
'''

driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/basic-home/div/div/div[1]/tour/div[7]/div[1]').click()

time.sleep(4)

'''
Here we will actually go in and click all the cards which have "yes" or "no" 
to "yes" and ignore others
'''

sameNames = driver.find_elements_by_class_name('home-healthy-habit-icon')
count = 1
for elem in sameNames:
	print("elem is:",elem.get_attribute("class"))
	ActionChains(driver).move_to_element(elem).perform()
	time.sleep(2)
	print("it reached after sleep")
	try:
		print("Value of count:",count)
		hiddenYes = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/basic-home/div/div/div[2]/home-healthy-habits/div/div/div[%d]/home-healthy-habit-tile/div/div[2]/button[1]' % count)
		ActionChains(driver).click(hiddenYes).perform()
	except NoSuchElementException:
		print("nvm")
	count = count+1




