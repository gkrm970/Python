from datetime import datetime
import os

import pytest
from selenium import webdriver


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


########### pytest HTML Report ################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "Opencart"
    config._metadata["Module Name"] = "CustRegistration"
    config._metadata["Tester"] = "Pavan"


# It is hooked for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Specifying report folder location and save a report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (
        os.path.abspath(os.curdir)
        + "\\reports\\"
        + datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        + ".html"
    )
