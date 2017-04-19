#Adding comment to test gerrithub
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime



class VirginPulseAuto:
	def __init__(self, driver, link, user, password):
		self.link = link
		self.user = user
		self.password = password
		self.driver = driver


	def visit_url(self):
		self.driver.get(self.link)

	def login_into_virginpulse(self):
		self.driver.find_element_by_id('oUserID').send_keys(self.user + Keys.TAB)
		self.driver.find_element_by_id('oPwdID').send_keys(self.password)
		time.sleep(1)
		self.driver.find_element_by_id('oLogon').click()
		time.sleep(10)

	def element_is_visible(self):
		timeout = 5
		try:
			element_present = EC.presence_of_element_located((By.ID, 'close-trophy-popup-wrapper'))
			WebDriverWait(self.driver, timeout).until(element_present)
		except TimeoutException:
			print "Timed out waiting for page to load"

	def close_trophy_popup(self):
		try:
			elem = self.driver.find_element_by_class_name('close-trophy-popup-wrapper')
			if elem.is_displayed():
				elem.click()
				print("Zoom in 4x. Successful")
			else:
				print("Element is not visible")
		except NoSuchElementException:
			print("No such thing")

	def check_daily_cards(self):
		categoryIds = self.driver.find_elements_by_xpath("//*[@id=\"triggerCloseCurtain\"]")
		cnt = 2
		for id in categoryIds:
			numId = id.get_attribute('category')
			print("numid: ", int(str(numId)))
			hitId = self.driver.find_element_by_xpath("//*[@category=" + numId + "]")
			ActionChains(self.driver).click(hitId).perform()
			# try to click like button for testing
			hitLike = self.driver.find_element_by_xpath(
			"//*[@id=\"daily-tips-slider\"]/div[1]/daily-cards/div/div[3]/div[6]/img[" +
			str(cnt) + "]")
			ActionChains(self.driver).click(hitLike).perform()
			print("Should have clicked a button")
			nextButton = self.driver.find_element_by_xpath(
			    "//*[@id=\"page-wrapper\"]/div/div/div/basic-home/div/div/daily-tips/div/div[4]")
			ActionChains(self.driver).click(nextButton).perform()
			print("should have clicked next button")
			cnt = cnt - 1
			time.sleep(5)

	def click_healthy_habits_option(self):
		self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/basic-home/div/div/div[1]/tour/div[7]/div[1]').click()
		time.sleep(5)

	def check_healthy_habits(self):
		sameNames = self.driver.find_elements_by_class_name('home-healthy-habit-icon')
		count = 1
		for elem in sameNames:
			print("elem is:", elem.get_attribute("class"))
			ActionChains(self.driver).move_to_element(elem).perform()
			time.sleep(2)
			try:
				print("Value of count:", count)
				hiddenYes = self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div/div/basic-home/div/div/div[2]/home-healthy-habits/div/div/div[%d]/home-healthy-habit-tile/div/div[3]/button[1]' % count)
				ActionChains(self.driver).click(hiddenYes).perform()
			except NoSuchElementException:
				print("No Healthy habits which have \"yes\" or \"no\" option")
			count = count + 1

	def close_browser(self):
		self.driver.close()



#driver = webdriver.Chrome()
driver = webdriver.Chrome('/Users/ripudamanflora/Downloads/chromedriver')

vgPulse = VirginPulseAuto(driver, 'https://member.virginpulse.com/login.aspx', '<ENTER USERNAME>', '<ENTER PASSWORD>')
vgPulse.visit_url()
vgPulse.login_into_virginpulse()

#make sure element is visible
vgPulse.element_is_visible()

#Close trophy pop up
vgPulse.close_trophy_popup()

#Check the daily cards
vgPulse.check_daily_cards()

#Click healthy card check option
vgPulse.click_healthy_habits_option()

#Click "Yes" for healthy habits
vgPulse.check_healthy_habits()

#Close the browser
vgPulse.close_browser()










