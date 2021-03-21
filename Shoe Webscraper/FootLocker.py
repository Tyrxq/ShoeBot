from Drivers import chromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
def openFootLocker():
    chromeDriver.get("https://www.footlocker.com")



if __name__ == "__main__":
    openFootLocker()
