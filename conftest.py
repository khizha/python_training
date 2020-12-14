
from fixture.application import Application
import pytest
import json

# global variable containing fixture
fixture = None

# global variable containing configuration file data
target = None

@pytest.fixture()
#@pytest.fixture(scope = "session")

def app(request):
    # use the global variable "fixture"
    global fixture
    global target

    browser = request.config.getoption("--browser")

    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)

    # check if fixture does not exist or is corrupted/invalid
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
