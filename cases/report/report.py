from .. import *

def message():
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    driver = webdriver.Edge()
    url = 'https://kworks.krx.co.kr/main.act'
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(
            (By.NAME,"userid")
        )
    )

    driver.find_element(By.NAME,"userid").send_keys('smart')
    driver.find_element(By.NAME,"password").send_keys('gksrnrrjfoth1!')
    driver.find_element(By.XPATH,'//*[@id="kLogin_wrap"]/form/div/div[2]/div[2]/div[4]/button').click()

    selenium_util.click(driver,By.ID,'organizationTopButton')
    selenium_util.click(driver,By.ID,'person_220054')
    selenium_util.click(driver,By.XPATH,'//*[@id="tempPopup"]/div/div/div/div[4]/button[3]')
    selenium_util.click(driver,By.XPATH,'/html/body/div[78]/div/div/div/div[5]/div/section/article/div[2]/div[2]/button[2]')

    driver.switch_to.window(driver.window_handles[-1])

    wait.until(
        EC.presence_of_element_located(
            (By.ID,'sendNumber')
        )
    )
    Select(driver.find_element(By.ID,'sendNumber')).select_by_value('02-3774-4336')

    driver.find_element(By.ID,'numInputType2').click()

    selenium_util.write(driver,By.ID,'receiveNum',
        "01048117860,01047832352,01094709217,"
        +"01092396176,01039271392,01035280385,"
        +"01046314765,01037067995,01072021479,01030144166,"
        +"01040861951,01071192516,01033001038,01049386800"
    )
    
    driver.find_element(By.ID,'sendMassage').send_keys(  
        datetime.today().strftime("%m.%d")+"[스마트워크]스마트워크시스템 정상가동 *"+config['username']+", "+config['coworker']
    )

    time.sleep(1)

    win32api.MessageBox(0,"발송을 원하시면 확인을 눌러주세요","메시지 발송확인",win32con.MB_OK)

    selenium_util.click(driver,By.XPATH,'//*[@id="sendPush"]/div[4]/table/tbody/tr/td[2]/a')

    time.sleep(60)

def page():
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    driver = webdriver.Edge()
    url = "http://iticc.krx.co.kr:7101/"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    selenium_util.change_frame(driver,By.XPATH,"/html/frameset/frame[2]")

    wait.until(
        EC.presence_of_element_located(
            (By.NAME,"loginID")
        )
    )
    driver.find_element(By.NAME,"loginID").send_keys('smartpm01')
    driver.find_element(By.NAME,"loginPwd").send_keys('gksrnrrjfoth1!')
    driver.find_element(By.NAME,"loginPwd").send_keys(Keys.RETURN)
    
    selenium_util.change_frame(driver,By.XPATH,"/html/frameset/frame[1]")
    selenium_util.click(driver,By.XPATH,'//*[@id="winSize"]/tbody/tr/td/table/tbody/tr[2]/td[3]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/a')
    
    driver.switch_to.default_content()

    selenium_util.change_frame(driver,By.XPATH,"/html/frameset/frame[2]")
    selenium_util.change_frame(driver,By.XPATH,"/html/frameset/frame[2]")

    selenium_util.change_frame(driver,By.XPATH,"/html/body/table/tbody/tr/td[2]/iframe")

    driver.set_window_size(1800,1000)

    selenium_util.click(driver,By.XPATH,'//*[@id="winSize"]/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td[3]/a[2]')

    selenium_util.write(driver,By.XPATH,'//*[@id="winSize"]/tbody/tr[6]/td/table[2]/tbody/tr[2]/td[2]/input',config['username'])

    for i,j in [(1,12),(3,19),(4,2)]:
        for k in range(j):
            driver.find_element(By.ID,'SMW_0'+str(i)+'_'+str(k+1)).click()

    driver.find_element(By.XPATH,'//*[@id="winSize"]/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/a[1]').click()
    
    time.sleep(1)

    driver.switch_to.alert.accept()
    
    time.sleep(1)
