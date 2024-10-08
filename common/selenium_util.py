from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click(driver,selector,locate):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (selector,locate)
        )
    )
    driver.find_element(selector,locate).click()


def write(driver,selector,locate,text):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (selector,locate)
        )
    )
    driver.find_element(selector,locate).send_keys(text)


def change_frame(driver,selector,locate):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (selector,locate)
        )
    )
    driver.switch_to.frame(driver.find_element(selector,locate))