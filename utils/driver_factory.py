from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.config import BROWSER, EXECUTION_MODE, GRID_URL


def get_driver():

    if BROWSER.lower() == "chrome":
        options = ChromeOptions()

        if EXECUTION_MODE == "remote":
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=options
            )
        else:
            driver = webdriver.Chrome(options=options)

    elif BROWSER.lower() == "edge":
        options = EdgeOptions()

        if EXECUTION_MODE == "remote":
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=options
            )
        else:
            driver = webdriver.Edge(options=options)

    elif BROWSER.lower() == "firefox":
        options = FirefoxOptions()

        if EXECUTION_MODE == "remote":
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=options
            )
        else:
            driver = webdriver.Firefox(options=options)

    else:
        raise Exception("Unsupported browser")

    driver.maximize_window()

    return driver