from .. import *

def reserve(driver):
    result = False

    selenium_util.click(driver,By.ID,'saehaButton')

    driver.switch_to.window(driver.window_handles[-1])

    selenium_util.click(driver,By.XPATH,'//*[@id="appRoot"]/div/div/ul/li[2]/div[2]')
    
    driver.close()

    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(1)
    if len(driver.window_handles) == 3 :
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[2]')

    names = driver.find_elements(By.XPATH,'/html/body/div[2]/div/h2')

    if len(names) == 4 :
        result = True

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    return result