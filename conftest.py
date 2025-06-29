import os
import pytest
import tempfile
from selenium import webdriver


@pytest.fixture
def driver(request, browser):
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        
        # ✅ Use a fresh temporary profile
        tmp_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={tmp_dir}")
        
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        edge_options = webdriver.EdgeOptions()
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
