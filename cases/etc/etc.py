from .. import *
from . import *

def test():
    with open('./config.yml','r',encoding='UTF8') as f:
        config = yaml.full_load(f)

    result = {}
    
    driver = selenium_util.getDriver()
    url = 'https://kworks.krx.co.kr/main.act'
    driver.get(url)

    wait = WebDriverWait(driver, 60)

    selenium_util.write(driver,By.NAME,'userid',config['checker']['id'])
    driver.find_element(By.NAME,"password").send_keys(config['checker']['pw'])
    driver.find_element(By.XPATH,'//*[@id="kLogin_wrap"]/form/div/div[2]/div[2]/div[4]/button').click()

    messenger(driver)

    result['보고'] = bogo(driver,wait)
    result['플래너'] = plan(driver,wait)
    result['게시판'] = board(driver,wait)
    result['차량|회의실'] = reserve(driver)
    result['통합검색'] = search(driver,wait)
    result['메신저'] = messenger_check()
    
    driver.quit()

    return result