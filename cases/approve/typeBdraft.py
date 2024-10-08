from .. import *
from . import attachFile
from . import setDraftInfo

def draft(driver,wait):
    selenium_util.change_frame(driver,By.ID,'mainFrame')
    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[1]')
    selenium_util.click(driver,By.XPATH,'//*[@id="left"]/div[2]/p[1]')

    driver.switch_to.window(driver.window_handles[-1])

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'[id=spn_FormTreeView_0_0]')
        )
    )
    formContainerList = driver.find_elements(By.CSS_SELECTOR,'[id*="spn_FormTreeView_0_"]')

    formContainerDict = {}
    for formContainer in formContainerList :
        formContainerDict[formContainer.text]=formContainer.get_attribute('id')

    driver.find_element(By.ID,formContainerDict["IT"]).click()

    formList = driver.find_elements(By.CSS_SELECTOR,'[id*="lvtForm_TR_"]')
    formDict = {}
    for form in formList :
        formDict[form.get_attribute('data6')]=form.get_attribute('id')

    ActionChains(driver).double_click(
        driver.find_element(By.ID,formDict["작업 보고서"])
    ).perform()

    driver.switch_to.window(driver.window_handles[-1])
    
    selenium_util.change_frame(driver,By.ID,'message')
    
    testText = "일일점검_"+datetime.today().strftime("%m%d")+"_작업보고서"
    selenium_util.write(driver,By.ID,'frame_doctitle',testText)
    selenium_util.change_frame(driver,By.ID,'iframe_content')

    driver.find_element(By.ID, 'control1').send_keys('테스트 데이터')
    driver.find_element(By.ID, 'control2').send_keys('테스트 데이터')

    driver.switch_to.default_content()

    setDraftInfo.step(driver,wait)

    selenium_util.click(driver,By.ID,'btnSendDraft')
    selenium_util.change_frame(driver,By.ID,'iFrameLayer')
    selenium_util.click(driver,By.ID,'Submit1')
    
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[-1])

    driver.switch_to.default_content()