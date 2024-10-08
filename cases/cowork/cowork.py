from .. import *

def test():
    try:
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

        selenium_util.click(driver,By.ID,'projectButton')

        driver.switch_to.window(driver.window_handles[-1])

        selenium_util.click(driver,By.ID,'project-200526')

        selenium_util.click(driver,By.XPATH,'//*[@id="createPostUl"]/li[1]')

        wait.until(
            EC.element_to_be_clickable(
                (By.ID,'postTitle')
            )
        )
        driver.find_element(By.ID,'postTitle').send_keys("일일점검_"+datetime.today().strftime("%m%d"))
        driver.find_element(By.ID,'postCntn').click()
        ActionChains(driver).key_down(Keys.CONTROL) .send_keys('v').key_up(Keys.CONTROL).perform()

        selenium_util.click(driver,By.XPATH,'//*[@id="postPopup"]/div[1]/div/div[2]/div[5]/ul/li[1]/button')
        selenium_util.click(driver,By.XPATH,'//*[@id="postPopup"]/div[1]/div/div/div[5]/ul/li[1]/div/button[2]')
        time.sleep(3)

        path = r"K:\공유받은 폴더\외주인력폴더\일일점검"
        item = f"일일점검_{datetime.today().strftime('%Y%m%d')}.docx"

        upload_util.popupControl(path+"\\"+item,"협업")

        time.sleep(2)

        # endphaes
        driver.find_element(By.XPATH,'//*[@id="postPopup"]/div[1]/div/div/div[5]/div/button').click()

        time.sleep(3)

        driver.refresh()

        # check
        wait.until(
            EC.element_to_be_clickable(
                (By.ID,'detailUl')
            )
        )
        result = driver.find_element(By.XPATH,'//*[@id="detailUl"]/li[1]/div[2]/div[2]/div/div[3]/div[1]/h4').text

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()

        return "일일점검_"+datetime.today().strftime("%m%d") in result
    except Exception as ex:
        print("@@@@@@@@@@@협업 실패@@@@@@@@@@@")
        print(ex)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return False