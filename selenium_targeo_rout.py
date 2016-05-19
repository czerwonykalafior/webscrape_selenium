#!/usr/bin/python
# -*- coding: utf8 -*-
"""
Give your 'form' and ' to'. Application will check daily
the rout and save the result. After a/home/stiven/PycharmProjects/WebScraping02 given time (e.g month)
e-mail wil be send with results.

"""

import csv
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def write_to_csv(time_of_travel, start, end):
    acctual_date = time.time()
    result = [time_of_travel, acctual_date, start, end]

    # write the result to a file 'rout.cvs'
    with open('rout.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(result)
        f.close()


def init_webdriver():
    # driver = webdriver.Chrome("/home/stiven/PycharmProjects/WebScraping02/chromedriver")
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, start, end):
    url = "http://www.targeo.pl"
    driver.get(url)

    try:
        box_start = driver.wait.until(EC.presence_of_element_located((By.ID, "route_form_start")))
        box_end = driver.wait.until(EC.presence_of_element_located((By.ID, "route_form_end")))
        submit = driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@onclick='findroute()']")))

        box_start.send_keys(start)
        box_end.send_keys(end)
        submit.click()
        time_of_travel = driver.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "targeo-route-info-eta"))).text

        print("writing")
        write_to_csv(time_of_travel, start, end)

    except TimeoutException:
        print("".join(("Can find elements on ", url)))


if __name__ == "__main__":
    driver = init_webdriver()
    lookup(driver, "kraków, chodkiewicza", "zabierzów")
    driver.quit()
