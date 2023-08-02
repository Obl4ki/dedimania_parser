from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


driver = None


def init_driver():
    global driver  # treat as module singleton
    if not driver:
        opts = Options()
        opts.add_argument("--headless=new")

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))

    return driver
