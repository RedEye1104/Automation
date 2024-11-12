import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the desired URL
driver.get("https://www.easemytrip.com/hotels/")

driver.maximize_window()

AdClose = driver.find_element(By.XPATH,'//*[@id="login_pp"]/div/a')
AdClose.click()

#------------------------------------- Search Section -----------------------------------------------------------------

SearchLocation = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[3]/div/form/div/div[2]/span[1] ")
SearchLocation.click()
time.sleep(2)

NameSearch = driver.find_element(By.XPATH,'//*[@id="txtCity"]')
NameSearch.send_keys("New Delhi")
time.sleep(3)

SelectCity = driver.find_element(By.XPATH,'//*[@id="ui-id-1"]/li[1]')
SelectCity.click()
time.sleep(3)

#------------------------------------ Calander section ----------------------------------------------------------------

calendar = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/div/select[1]')
calendar.click()

month = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/div/select[1]/option[5]')
month.click()

Checkin = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[5]/td[1]')
Checkin.click()
CheckOut = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/table/tbody/tr[5]/td[2]')
CheckOut.click()
#-----------------------------------Guest/Room section-----------------------------------------------------------------

SelectRoom = driver.find_element(By.ID,'exithotelroom')
SelectRoom.click()
#-----------------------------------Search section----------------------------------------------------------------------

Search = driver.find_element(By.ID,'btnSearch')
Search.click()

#-----------------------------------Listing Page------------------------------------------------------------------------

ListingScroll = driver.execute_script("window.scrollBy(0, 500)")

ListingSelect = driver.find_element(By.XPATH,'//*[@id="hotelListDiv"]/div/div[4]/div[3]/div[2]/div/div[2]/div[2]/a/div')
ListingSelect.click()






time.sleep(5)