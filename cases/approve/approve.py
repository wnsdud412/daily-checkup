from .. import *
from . import typeAdraft
from . import typeBdraft
from . import reject

def test():
    try:
        driver = webdriver.Edge()
        url = 'https://kgw.krx.co.kr:8443/user/login/login.do'
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        # 기안
        selenium_util.write(driver,By.ID,"uid",'smart')
        driver.find_element(By.ID,"upw").send_keys('gksrnrrjfoth1!')
        driver.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/p[4]/label').click()

        typeAdraft.draft(driver,wait)
        typeBdraft.draft(driver,wait)

        # 로그아웃
        selenium_util.change_frame(driver,By.ID,'topFrame')
        selenium_util.click(driver,By.ID,'util_logout')

        # 반려
        selenium_util.write(driver,By.ID,"uid",'230284')
        driver.find_element(By.ID,"upw").send_keys('gksrnrrjfoth1!')
        driver.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/p[4]/label').click()

        reject.reject(driver,wait)

        # 로그아웃
        selenium_util.change_frame(driver,By.ID,'topFrame')
        selenium_util.click(driver,By.ID,'util_logout')

        #확인
        selenium_util.write(driver,By.ID,"uid",'smart')
        driver.find_element(By.ID,"upw").send_keys('gksrnrrjfoth1!')
        driver.find_element(By.XPATH,'//*[@id="loginForm"]/fieldset/p[4]/label').click()

        selenium_util.change_frame(driver,By.ID,'mainFrame')
        selenium_util.change_frame(driver,By.XPATH,'/html/frameset/frame[1]')

        wait.until(
            EC.presence_of_element_located(
                (By.ID,'DocList_TR_0')
            )
        )
        testDraft = driver.find_element(By.ID,'DocList_TR_0')

        if ( '일일점검_'+datetime.today().strftime("%m%d") in testDraft.find_element(By.XPATH,'./td[1]').get_attribute('title')
            and testDraft.get_attribute('data10') == '004') :
            return True
        else :
            return False
    except Exception as ex:
        print("@@@@@@@@@@@전자결재 실패@@@@@@@@@@@")
        print(ex)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return False
