import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.find_element(By.XPATH, "//input[@value='radio1']").click()
    driver.find_element(By.ID, "autocomplete").send_keys("Shakeer")
    ddexam = driver.find_element(By.ID, "dropdown-class-example")
    dde = Select(ddexam)
    dde.select_by_visible_text("Option1")
    checks = driver.find_element(By.XPATH, "//input[@id='checkBoxOption1']")
    checks.click()
    #driver.find_element(By.ID, "openwindow").click()

except Exception as e:
    print(e)
else:
    pass
finally:
    time.sleep(4)
    driver.close()
