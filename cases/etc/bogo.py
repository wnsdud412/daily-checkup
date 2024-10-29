from .. import *

def bogo(driver,wait):
    result = False

    selenium_util.click(driver,By.ID,'bogoButton')

    selenium_util.switch_new_window(driver)

    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frameset/frame[2]')

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="listFrm"]/h1')
        )
    )
    if "보고" == driver.find_element(By.XPATH,'//*[@id="listFrm"]/h1').text :
        result = True

    driver.close()

    selenium_util.switch_new_window(driver)

    return result