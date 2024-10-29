from .. import *

def board(driver,wait):
    result = False

    selenium_util.click(driver,By.ID,'boardButton')

    selenium_util.switch_new_window(driver)

    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frameset/frame[2]')

    wait.until(
        EC.presence_of_element_located(
            (By.ID,'BoardListDiv')
        )
    )
    
    if len(driver.find_element(By.ID,'BoardListDiv').find_elements(By.TAG_NAME,'tr')) > 5 :
        result = True

    driver.close()
    selenium_util.switch_new_window(driver)
    
    return result