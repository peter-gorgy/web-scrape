from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    service = Service(executable_path="chromedriver")

    # Set options to make browsing easier.
    options = webdriver.ChromeOptions()
    
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url="https://www.saucedemo.com/")
    return driver

def clean_text(text):
    """This function is to extract the temperature in float

    Args:
        text (_type_): dynamic temperature.
    """
    temperature = text.split("$")[-1]
    return temperature

if __name__ == "__main__":

    driver = get_driver()
    print("***********************************")
    print(f"Current URL: {driver.current_url}")
    print(f"Title: {driver.title}")
    username = driver.find_element(by="xpath", value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
    username.send_keys("standard_user")
    password = driver.find_element(by="xpath", value="/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
    password.send_keys("secret_sauce")
    login = driver.find_element(by="id", value="login-button")
    login.click()
    print(f"Current URL: {driver.current_url}")
    print(f"Title: {driver.title}")

    item = driver.find_element(by="xpath", value="/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
    print(item.text)
    price = driver.find_element(by="xpath", value="/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div")
    print(clean_text(price.text))

    print("***********************************")
    time.sleep(15)