from .. import *
from . import attachFile
from . import setDraftInfo

def draft(driver,wait):
    selenium_util.change_frame(driver,By.ID,'mainFrame')
    selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[1]')
    selenium_util.click(driver,By.XPATH,'//*[@id="left"]/div[2]/p[1]')

    driver.switch_to.window(driver.window_handles[-1])

    selenium_util.click(driver,By.XPATH,'/html/body/div[3]/a[1]')

    driver.switch_to.window(driver.window_handles[-1])

    selenium_util.change_frame(driver,By.ID,'message')

    time.sleep(3)

    with open(r"cases\approve\inner.js",'r',encoding='UTF8') as inner:
        driver.execute_script(inner.read())
    
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)

    driver.switch_to.default_content()

    selenium_util.click(driver,By.ID,'btnFileAttach')
    selenium_util.change_frame(driver,By.ID,'iFrameLayer')
    selenium_util.click(driver,By.ID,'btn_AttachAdd')

    time.sleep(1)

    path = r"K:\공유받은 폴더\외주인력폴더\일일점검"
    item = f"일일점검_{datetime.today().strftime('%Y%m%d')}.docx"

    upload_util.popupControl(path+"\\"+item,"기안")

    selenium_util.click(driver,By.ID,'btn_AttachSaveSure')

    driver.switch_to.default_content()

    time.sleep(1)
    
    setDraftInfo.step(driver,wait)

    time.sleep(1)

    # endphase
    selenium_util.click(driver,By.ID,'btnSendDraft')
    selenium_util.change_frame(driver,By.ID,'iFrameLayer')
    selenium_util.click(driver,By.ID,'Submit1')
    
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[-1])







