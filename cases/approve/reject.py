from .. import *


def reject(driver,wait):
    
    for tt in ["내부결재","작업보고서"] :
        selenium_util.change_frame(driver,By.ID,'mainFrame')
        selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[2]')

        draftList = driver.find_elements(By.NAME,'DocList_TR')
        testText = '일일점검_'+datetime.today().strftime("%m%d")+"_"+tt

        for draft in draftList :
            if testText == draft.find_element(By.XPATH,'./td[1]').text :
                ActionChains(driver).double_click(draft).perform()

                currentHandle = driver.current_window_handle

                driver.switch_to.window(driver.window_handles[-1])

                selenium_util.change_frame(driver,By.ID,'iFrameLayer')
                selenium_util.click(driver,By.ID,'Submit1')

                driver.switch_to.default_content()

                selenium_util.click(driver,By.ID,'btnReject')
                selenium_util.change_frame(driver,By.ID,'iFrameLayer')

                selenium_util.click(driver,By.ID,'Submit1')
                selenium_util.change_frame(driver,By.ID,'iFrameLayer')

                selenium_util.write(driver,By.ID,'txt_OpinionContent',testText)

                driver.find_element(By.ID,"bbtn_OpinionSave").click()

                driver.switch_to.default_content()
                driver.switch_to.frame(driver.find_element(By.ID,'iFrameLayer'))
                driver.switch_to.frame(driver.find_element(By.ID,'iFrameLayer'))

                selenium_util.click(driver,By.ID,'Submit1')

                driver.switch_to.default_content()
                time.sleep(1)

                driver.switch_to.frame(driver.find_element(By.ID,'iFrameLayer'))

                selenium_util.click(driver,By.ID,"bbtn_OpinionOK")

                driver.switch_to.default_content()
                
                time.sleep(1)

                driver.switch_to.frame(driver.find_element(By.ID,'iFrameLayer'))

                selenium_util.click(driver,By.ID,'Submit1')
                
                time.sleep(1)

                driver.switch_to.window(currentHandle)

                break