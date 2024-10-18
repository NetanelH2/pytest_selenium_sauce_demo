from selenium import webdriver


def configure_driver(driver: webdriver.Remote) -> webdriver.Remote:
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def get_chrome_driver() -> webdriver.Remote:
    driver = webdriver.Chrome()
    return configure_driver(driver)


def get_firefox_driver() -> webdriver.Remote:
    driver = webdriver.Firefox()
    return configure_driver(driver)
