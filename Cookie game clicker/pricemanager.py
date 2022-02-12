from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PriceManager:
    def __init__(self):
        chrome_driver_path = "/Applications/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")
        self.cookie = self.driver.find_element(By.ID, "cookie")
        self.score = self.driver.find_element(By.ID, "money")
        self.u1price = 15
        self.u2price = 100
        self.u3price = 500
        self.u4price = 2000
        self.u5price = 7000
        self.u6price = 50000
        self.u7price = 1000000
        self.u8price = 123456789
    def click(self):
        self.cookie.click()

    def formatprice(self, string):
        price = string.text.split("-")[1]
        price = price.replace(",", "")
        price = int(price)
        return price

    def checkupdate(self):
        self.money = self.score.text
        self.money = self.money.replace(",", "")
        self.money = int(self.money)
        if self.money > self.u8price:
            upgrade8 = self.driver.find_element(By.ID, "buyTime machine")
            upgrade8.click()
            time.sleep(0.5)
            self.u8price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[8]/b'))
        elif self.money > self.u7price:
            upgrade7 = self.driver.find_element(By.ID, "buyPortal")
            upgrade7.click()
            time.sleep(0.5)
            self.u7price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[7]/b'))
        elif self.money > self.u6price:
            upgrade6 = self.driver.find_element(By.ID, "buyAlchemy lab")
            upgrade6.click()
            time.sleep(0.5)
            self.u6price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[6]/b'))
        elif self.money > self.u5price:
            upgrade5 = self.driver.find_element(By.ID, "buyShipment")
            upgrade5.click()
            time.sleep(0.5)
            self.u5price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[5]/b'))
        elif self.money > self.u4price:
            upgrade4 = self.driver.find_element(By.ID, "buyMine")
            upgrade4.click()
            time.sleep(0.5)
            self.u4price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[4]/b'))
        elif self.money > self.u3price:
            upgrade3 = self.driver.find_element(By.ID, "buyFactory")
            upgrade3.click()
            time.sleep(0.5)
            self.u3price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[3]/b'))
        elif self.money > self.u2price:
            upgrade2 = self.driver.find_element(By.ID, "buyGrandma")
            upgrade2.click()
            time.sleep(0.5)
            self.u2price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[2]/b'))
        elif self.money > self.u1price:
            upgrade1 = self.driver.find_element(By.ID, "buyCursor")
            upgrade1.click()
            time.sleep(0.5)
            self.u1price = self.formatprice(self.driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[1]/b'))








