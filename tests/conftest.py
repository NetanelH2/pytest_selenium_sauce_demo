import pytest
from selenium import webdriver
from typing import Generator

from utils.driver_factory import (
    get_chrome_driver,
    get_firefox_driver,
)
from data.user_data import user_data
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"], scope="session")
def driver(request: pytest.FixtureRequest) -> Generator[webdriver.Remote, None, None]:
    if request.param == "chrome":
        driver: webdriver.Remote = get_chrome_driver()
    elif request.param == "firefox":
        driver: webdriver.Remote = get_firefox_driver()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_fixture(driver: webdriver.Remote) -> webdriver.Remote:
    valid_user_data: tuple[str, str, str] = user_data[0]

    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_user(*valid_user_data[:2])

    assert login_page.verify_successful_login()
    return driver
