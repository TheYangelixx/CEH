from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a webdriver object for Chrome
driver = webdriver.Chrome()

# Open the website
url = 'https://www.weblite.me/'
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/input').click()

phoneNum = '09112342131'
driver.find_element(By.NAME, 'phone').send_keys(phoneNum)

btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[2]/button/span')))
btn.click()

driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[3]/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[3]/input[1]').send_keys('0')
time.sleep(100)
# driver.find_element(By.XPATH,'//*[@id="signin-options"]/div/div[1]/a[1]/span[2]').click()


# Find the input fields and enter the registration information
# username_field = driver.find_element_by_name('username')
# username_field.send_keys('my_username')

# email_field = driver.find_element_by_name('email')
# email_field.send_keys('my_email@example.com')

# password_field = driver.find_element_by_name('password')
# password_field.send_keys('my_password')

# # Find the button or link element and click it to submit the registration form
# submit_button = driver.find_element_by_name('submit')
# submit_button.click()

# # Wait for the page to load after submitting the form
# time.sleep(5)

# # Close the browser window
# driver.quit()