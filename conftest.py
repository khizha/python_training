
from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle

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

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())