from .. import *

def plan(driver,wait):
    result = False

    selenium_util.click(driver,By.ID,'planButton')
    
    selenium_util.switch_new_window(driver)

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
    selenium_util.switch_new_window(driver)
    
    return result