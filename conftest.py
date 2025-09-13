import pytest
import pytest_html.extras
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="Type in browser name: chrome or edge")


@pytest.fixture(scope="function")
def browser(request):
    bd = request.config.getoption("--browser")
    if bd == "chrome":
        driver = webdriver.Chrome()
    else:
        service = Service(executable_path="C:\\Users\hp\PycharmProjects\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    driver.get("http://localhost:100")
    request.node.driver = driver
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_file)

            if screenshot_file:
                extra = getattr(report, "extra", [])
                html = (f'<div><img src="{screenshot_file}" alt="screenshot" style="width:300px;height:200px;" '
                        f'onclick="window.open(this.src)" /></div>')
                extra.append(pytest_html.extras.html(html))
                report.extra = extra


@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

