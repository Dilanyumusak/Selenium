# Seçeceğiniz bir web sitesine giriş yapmak için gerekli, 
# hatalı giriş ve doğru giriş olrak iki farklı senaryoyu test eden selenium kodlar

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Başarılı Senaryo
driver = webdriver.Chrome()
driver.get("https://tr.pinterest.com/")
driver.maximize_window()
sleep(3)

lgnBtn = driver.find_element(By.XPATH,"//*[@id='fullpage-wrapper']/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div")
lgnBtn.click()
sleep(5)

userMail = driver.find_element(By.XPATH,"//*[@id='email']")
userPassword = driver.find_element(By.XPATH,"//*[@id='password']")

userMail.send_keys("pair4etiya@hotmail.com")
userPassword.send_keys("1234_Ety")
sleep(2)

lgnBtn2 = driver.find_element(By.XPATH,"//*[@id='__PWS_ROOT__']/div/div[1]/div/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div")
lgnBtn2.click()
sleep(5)

title = driver.title

if title == "Pinterest":
   print("Giriş Başarılı 👍")
else:
   print("Giriş Başarısız 😢")

driver.close()

# Başarısız Senaryo
driver = webdriver.Chrome()
driver.get("https://tr.pinterest.com/")
driver.maximize_window()
sleep(3)

lgnBtn = driver.find_element(By.XPATH,"//*[@id='fullpage-wrapper']/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div")
lgnBtn.click()
sleep(5)

userMail = driver.find_element(By.XPATH,"//*[@id='email']")
userPassword = driver.find_element(By.XPATH,"//*[@id='password']")

userMail.send_keys("pair4etiya")
userPassword.send_keys("1234_Ety")
sleep(2)

lgnBtn2 = driver.find_element(By.XPATH,"//*[@id='__PWS_ROOT__']/div/div[1]/div/div[2]/div/div/div/div/div/div[4]/form/div[7]/button/div")
lgnBtn2.click()
sleep(5)

title = driver.title

if title == "Pinterest":
   print("Giriş Başarılı 👍")
else:
   print("Giriş Başarısız 😢")
