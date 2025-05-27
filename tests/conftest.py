import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

import os
from appium import webdriver
import allure_commons
from selene import browser, support
from config import config

@pytest.fixture(scope='function')
def android_management():
    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": config.app, # по умолчанию запускается википедия?

        'bstack:options': {
            "projectName": "QA Guru Homework Project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": config.username,
            "accessKey": config.accessKey}
    })
    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    session_id = browser.driver.session_id
    yield
    browser.quit()

@pytest.fixture(scope='function')
def ios_management():
    options = XCUITestOptions().load_capabilities({
        "platformName": "ios",
        "platformVersion": "13",
        "deviceName": "iPhone 11",
        "app": config.app,

        'bstack:options': {
            "projectName": "QA Guru Homework Project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName":  config.username,
            "accessKey": config.accessKey}
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    session_id = browser.driver.session_id
    yield
    browser.quit()