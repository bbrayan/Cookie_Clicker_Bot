from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")


driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(15,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

def upgradeF(X):
    upgrade_actions = ActionChains(driver)
    upgrade_actions.move_to_element(X)
    upgrade_actions.click()
    upgrade_actions.perform()


for i in range(9999999):
    for i in range(20):
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
    for item in items:
        if item.text.isnumeric():
            value = int(item.text)
            if value <= count:
                upgradeF(item)
    upgradeF(driver.find_element_by_id("upgrade0"))


