from .. import *


def setDocInfo(driver,wait) :
    selenium_util.click(driver,By.ID,'showDocinfo')
    selenium_util.click(driver,By.XPATH,'//*[@id="Docinfo"]/table[1]/tbody/tr[1]/td/a/span')

    currentHandle = selenium_util.switch_new_window(driver)

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
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    selenium_util.click(driver,By.ID,'btntotaldocinfo')

    currentHandle = selenium_util.switch_new_window(driver)

    userList = driver.find_elements(By.NAME,'pUserList_TR')

    for user in userList :
        if config['pm']['name'] == user.get_attribute('data4') :
            ActionChains(driver).double_click(user).perform()

    setDocInfo(driver,wait)

    driver.switch_to.window(currentHandle)



    
    
