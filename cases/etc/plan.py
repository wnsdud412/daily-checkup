from .. import *

def plan(driver,wait):
    result = False

    selenium_util.click(driver,By.ID,'planButton')
    
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(0.5)
    
    wait.until(
        EC.invisibility_of_element_located(
            (By.XPATH,'//*[@id="js-loading-popup"]/div/div/div/div[2]')
        )
    )

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="mainTop"]/div')
        )
    )
    if "내 플래너" == driver.find_element(By.XPATH,'//*[@id="mainTop"]/div').text :
        result = True

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    return result