from .. import *

def messenger(driver):
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    selenium_util.click(driver,By.ID,'chattingTopButton')
    selenium_util.click(driver,By.ID,'contactBtn')
    selenium_util.write(driver,By.ID,'chattingSearchInput',config['user']['name'])
    selenium_util.click(driver,By.XPATH,'//*[@id="person_'+config['user']['id']+'"]/button')

    time.sleep(0.5)

    selenium_util.switch_new_window(driver)

    selenium_util.write(driver,By.XPATH,'//*[@id="messengerInput"]/div',"일일점검")
    selenium_util.click(driver,By.ID,'sendMessageButton')

    driver.close()
    selenium_util.switch_new_window(driver)


def messenger_check():
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    result = False
    
    driver = selenium_util.getDriver()
    url = 'https://kworks.krx.co.kr/main.act'
    driver.get(url)

    selenium_util.write(driver,By.NAME,'userid',config['user']['id'])
    driver.find_element(By.NAME,"password").send_keys(config['user']['pw'])
    driver.find_element(By.XPATH,'//*[@id="kLogin_wrap"]/form/div/div[2]/div[2]/div[4]/button').click()

    selenium_util.click(driver,By.ID,'chattingTopButton')
    selenium_util.click(driver,By.ID,'contactBtn')
    selenium_util.write(driver,By.ID,'chattingSearchInput',"스마트운영자")
    selenium_util.click(driver,By.XPATH,'//*[@id="person_'+config['checker']['id']+'"]/button')

    time.sleep(0.5)

    current_handle = selenium_util.switch_new_window(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID,"messengerUl")
        )
    )
    messages = driver.find_element(By.ID,"messengerUl")

    if '일일점검' == messages.find_element(By.XPATH,f'./li[{len(messages.find_elements(By.XPATH,"./li"))}]/div[2]/div[2]/div/div[1]/div[3]/div/div').text:
        result = True

    driver.close()
    driver.switch_to.window(current_handle)
    driver.close()

    return result