from .. import *

def search(driver,wait):
    result = False

    options=webdriver.EdgeOptions()
    options.add_argument("--headless")
    headless = selenium_util.getDriver(options)

    for i in range(1,4):
        headless.get(f"http://10.10.34.15{i}:6203")
        jsonData = json.loads(headless.find_element(By.XPATH,'/html/body/pre').text)
    
    headless.quit()

    selenium_util.click(driver,By.ID,'searchPopupTopButton')

    wait.until(
        EC.presence_of_element_located(
            (By.ID,'searchPopupInput')
        )
    )
    searchBar = driver.find_element(By.ID,'searchPopupInput')
    searchBar.send_keys("노동조합")
    searchBar.send_keys(Keys.ENTER)

    selenium_util.switch_new_window(driver)

    wait.until(
        EC.presence_of_element_located(
            (By.ID,'sortable')
        )
    )
    searchCounts = driver.find_elements(By.XPATH,'//*[@id="sortable"]/li/a/span')
    
    flag = True
    for searchCount in searchCounts:
        if int(searchCount.text.replace(',','')) < 0 :
            flag=False

    return flag