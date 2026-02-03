from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bot:

    def __init__(self, email, password):
        self.driver = webdriver.Chrome('D:\coding\Yangelixx\CEH\\bot\chromedriver.exe')

        self.email = email
        self.password = password

    def Login(self):
        driver = self.driver
        driver.get('https://www.imdb.com/')
        driver.maximize_window()
        driver.find_element(By.XPATH,'//*[@id="imdbHeader"]/div[2]/div[5]/a/div').click()
        btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="signin-options"]/div/div[1]/a[1]/span[2]')))
        btn.click()
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, 'signInSubmit'))
        driver.find_element(By.NAME, 'email').send_keys(self.email)
        driver.find_element(By.NAME, 'password').send_keys(self.password)
        btn.click()


bot1 = Bot('the_yangelixx@yahoo.com', 'yasna1385')
bot1.Login()