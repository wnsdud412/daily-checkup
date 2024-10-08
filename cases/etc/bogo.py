from .. import *

def bogo(driver,wait):
    result = False

    selenium_util.click(driver,By.ID,'bogoButton')

    driver.switch_to.window(driver.window_handles[-1])

    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frameset/frame[2]')

    wait.until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="listFrm"]/h1')
        )
    )
    if "보고" == driver.find_element(By.XPATH,'//*[@id="listFrm"]/h1').text :
        result = True

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    return result