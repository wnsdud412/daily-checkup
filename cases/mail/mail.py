from .. import *

def test():
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    try: 
        driver = webdriver.Edge()
        url = 'https://kmailin.krx.co.kr/'
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located(
                (By.ID,"member_id")
            )
        )

        driver.find_element(By.ID,"member_id").send_keys('smart')
        driver.find_element(By.ID,"member_pw").send_keys('gksrnrrjfoth1!')
        driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div/div[2]/div[2]/div[4]/input').click()

        selenium_util.click(driver,By.XPATH,'//*[@id="snb_mail"]/div/div[1]/a[1]')

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,'//*[@id="toDiv"]/ul')
            )
        )
        
        driver.find_element(By.XPATH,'//*[@id="toDiv"]/ul').find_element(By.TAG_NAME,'textarea').send_keys('양상철')
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="toDiv"]/ul').find_element(By.TAG_NAME,'textarea').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="ccDiv"]/ul').find_element(By.TAG_NAME,'textarea').send_keys(config['username'])
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="ccDiv"]/ul').find_element(By.TAG_NAME,'textarea').send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="subject"]').send_keys("일일점검"+datetime.today().strftime("%m%d"))

        path = r"K:\공유받은 폴더\외주인력폴더\일일점검"
        item = f"일일점검_{datetime.today().strftime('%Y%m%d')}.docx"

        selenium_util.click(driver,By.XPATH,'//*[@id="attachments-cell"]/div[1]/a')
        time.sleep(1)
        upload_util.popupControl(path+"\\"+item,"메일")
        
        selenium_util.click(driver,By.XPATH,'//*[@id="attachments-cell"]/div[1]/a')
        time.sleep(1)
        upload_util.popupControl(path+"\\"+item,"메일")

        driver.find_element(By.XPATH,'//*[@id="attachments-cell"]/div[2]/div[2]/ul/li[2]/span[5]/button').click()

        driver.find_element(By.ID,'tx_canvas_wysiwyg').click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        pyautogui.press('delete')
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        
        time.sleep(10)

        #endphaes
        driver.find_element(By.XPATH,'//*[@id="writeBtnMenu"]/div/div[1]/button[1]').click()
        driver.find_element(By.ID,'sendMailBtn').click()
        time.sleep(1)
        driver.close()

        driver = webdriver.Edge()
        url = 'https://kmailin.krx.co.kr/'
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.presence_of_element_located(
                (By.ID,"member_id")
            )
        )
        driver.find_element(By.ID,"member_id").send_keys(config['userid'])
        driver.find_element(By.ID,"member_pw").send_keys(config['userpw'])
        driver.find_element(By.XPATH,'//*[@id="wrap"]/form/div/div[2]/div[2]/div[4]/input').click()

        wait.until(
            EC.presence_of_element_located(
                (By.ID,"divList")
            )
        )
        mail_names = driver.find_elements(By.XPATH,'//*[@id="divList"]/div/div[1]/ol/li/div/div[2]/a[1]/span')

        for mail_name in  mail_names:
            if "일일점검"+datetime.today().strftime("%m%d") in mail_name.text :
                driver.close()
                return True

        driver.close()
        
        return False
    except Exception as ex:
        print("@@@@@@@@@@@메일 실패@@@@@@@@@@@")
        print(ex)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return False
    