from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def find_element(self, by, value: str) -> WebElement:
        return self.driver.find_element(by, value)

    def find_elements(self, by, value: str) -> List[WebElement]:
        return self.driver.find_elements(by, value)

    def is_text_present(self, text: str) -> bool:
        return text in self.driver.page_source

    def is_url_opened(self, url: str) -> bool:
        return url in self.driver.current_url
