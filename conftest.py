
from fixture.application import Application
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

# global variable containing fixture
fixture = None

# global variable containing configuration file data
target = None

def load_config(file):
    global target

    if target is None:
        # get path to the configuration file
        #if request.config.getoption("--targetpath") is None:
            # if the path to the configuration file is not provided in the command line then it is located in the current directory
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        #else:
            # if the path to the configuration file is provided
        #   config_file = os.path.join(request.config.getoption("--targetpath"), file)

        with open(config_file) as f:
            target = json.load(f)

    return target

@pytest.fixture()
#@pytest.fixture(scope = "session")

def app(request):
    # use the global variable "fixture"
    global fixture

    browser = request.config.getoption("--browser")

    web_config = load_config(request.config.getoption("--target"))['web']

    # check if fixture does not exist or is corrupted/invalid
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--targetpath", action="store", default=None)
    parser.addoption("--check_ui", action="store_true")

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