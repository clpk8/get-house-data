from selenium import webdriver
import csv
import time
import pandas as pd
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def appealed(str):
    pos = str.find(': ')
    char = str[pos + 2]
    print(char)
    if char.isdigit() and char != '0':
        return True
    else:
        return False


final = []
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

with open('output1.csv', 'r') as file:
    driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver", options= chrome_options)
    driver.get("https://projects.newsday.com/news/property-taxes-map/?")
    time.sleep(5)
    reader = csv.reader(file)
    wait = WebDriverWait(driver, 10)

    close = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div/div/span/span"))
    )
    close.click()
    for row in reader:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/section/div[3]/form/div/input")))
            search_box = driver.find_element_by_xpath("/html/body/div[1]/div[5]/section/div[3]/form/div/input")
            search_box.send_keys(row)
            search_box.submit()
            try:
                time.sleep(0.5)
                wait.until(EC.presence_of_element_located((By.XPATH,
                                                    "/html/body/div[1]/div[5]/section/section[2]/div/div/div[1]/article[1]/section/div[4]/ul/li[1]")))
                time.sleep(0.5)
                text = driver.find_element_by_xpath("/html/body/div[1]/div[5]/section/section[2]/div/div/div[1]/article[1]/section/div[4]/ul/li[1]")
                textStr = text.text
                if not appealed(textStr):
                    print(row[0] + " : " + textStr)
                    final.append(row[0])

                button = driver.find_element_by_xpath("/html/body/div[1]/div[5]/section/div[2]/a[1]")
                button.click()
            except:
                print("First exception")
                button = driver.find_element_by_xpath("/html/body/div[1]/div[5]/section/div[2]/a[1]")
                button.click()
        except:
            print("Second exception")
            continue

list = pd.Series(final)
list.to_csv("result1.csv", index=False)
