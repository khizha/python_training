
from fixture.application import Application
import pytest
import json
import os.path

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
        # get path to the configuration file
        if request.config.getoption("--targetpath") is None:
            # if the path to the configuration file is not provided in the command line then it is located in the current directory
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        else:
            # if the path to the configuration file is provided
            config_file = os.path.join(request.config.getoption("--targetpath"), request.config.getoption("--target"))

        with open(config_file) as f:
            target = json.load(f)

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
    parser.addoption("--targetpath", action="store", default=None)