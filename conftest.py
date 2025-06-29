import os
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def driver(request, browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        tmp_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={tmp_dir}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--headless=new")  # optional for CI
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("-headless")  # optional
        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")  # optional
        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests against: chrome, firefox, or edge")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
