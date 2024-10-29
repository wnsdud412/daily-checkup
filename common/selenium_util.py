from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
from . import system_util
import os
import time

def switch_new_window(driver):
    try : 
        currentHandle = driver.current_window_handle
    except NoSuchWindowException as e :
        currentHandle = 0
    
    for i in range(5):
        if currentHandle == driver.window_handles[-1] :
            time.sleep(1)
        else :
            driver.switch_to.window(driver.window_handles[-1])
            return currentHandle
    raise Exception('신규 팝업이 생성되지 않았습니다.')

def getDriver(options=None):
    service=Service(executable_path=os.path.join(system_util.resource_path(),'msedgedriver.exe'))
    if options == None:
        driver = webdriver.Edge(service=service)
    else :
        driver = webdriver.Edge(service=service,options=options)
    return driver

def click(driver,selector,locate):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (selector,locate)
        )
    )
    driver.find_element(selector,locate).click()


def write(driver,selector,locate,text):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (selector,locate)
        )
    )
    driver.find_element(selector,locate).send_keys(text)


def change_frame(driver,selector,locate):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (selector,locate)
        )
    )
    driver.switch_to.frame(driver.find_element(selector,locate))