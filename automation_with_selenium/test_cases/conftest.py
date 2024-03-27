import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver


# this will get the value from CLI/hooks - this is a special type of method
def pytest_addoption(parser):
    parser.addoption("--browser")


# this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
