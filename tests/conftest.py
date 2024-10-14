from typing import Any, Generator
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from data.user_data import user_data
from pages.login_page import LoginPage
from utils.driver_factory import get_driver


@pytest.fixture(scope="session")
def driver() -> Generator[WebDriver, Any, None]:
    driver: WebDriver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_fixture(driver: WebDriver) -> WebDriver:
    valid_user_data: tuple[str, str, str] = user_data[0]
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user(*valid_user_data[:2])
    assert login_page.verify_successful_login(), "Login failed"
    return driver
