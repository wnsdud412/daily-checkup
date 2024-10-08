from .. import *


def setDocInfo(driver,wait) :
    selenium_util.click(driver,By.ID,'showDocinfo')
    selenium_util.click(driver,By.XPATH,'//*[@id="Docinfo"]/table[1]/tbody/tr[1]/td/a')

    currentHandle = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1]) 

    wait.until(
        EC.presence_of_element_located(
            (By.ID,'spn_FromTreeView_0') 
        )
    )
    categoryList = driver.find_elements(By.CSS_SELECTOR,'[id*="spn_FromTreeView_"]')

    for category in categoryList :
        if "보안" in category.text :
            driver.find_element(By.ID,category.get_attribute('id')).click()
            break

    driver.find_element(By.XPATH,'/html/body/div[3]/a[1]').click()

    driver.switch_to.window(currentHandle)

    driver.find_element(By.ID,'rdoSecType25').click()

    driver.find_element(By.XPATH,'//*[@id="orgbtnArea"]/table/tbody/tr/td/div/a').click()


def step(driver,wait) :
    selenium_util.click(driver,By.ID,'btntotaldocinfo')

    currentHandle = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[-1])

    userList = driver.find_elements(By.NAME,'pUserList_TR')

    for user in userList :
        if '양상철' == user.get_attribute('data4') :
            ActionChains(driver).double_click(user).perform()

    setDocInfo(driver,wait)

    driver.switch_to.window(currentHandle)



    
    
