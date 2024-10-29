from .. import *

def reserve(driver):
    result = False

    selenium_util.click(driver,By.ID,'saehaButton')

    selenium_util.switch_new_window(driver)

    selenium_util.click(driver,By.XPATH,'//*[@id="appRoot"]/div/div/ul/li[2]/div[2]')
    
    driver.close()

    selenium_util.switch_new_window(driver)

    time.sleep(1)
    if len(driver.window_handles) == 3 :
        selenium_util.switch_new_window(driver)
        driver.close()
        selenium_util.switch_new_window(driver)

    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[2]')

    names = driver.find_elements(By.XPATH,'/html/body/div[2]/div/h2')

    if len(names) == 4 :
        result = True

    driver.close()
    selenium_util.switch_new_window(driver)

    return result