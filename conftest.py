
from fixture.application import Application
import pytest

# global variable containing fixture
fixture = None

@pytest.fixture()
#@pytest.fixture(scope = "session")

def app(request):
    # use the global variable "fixture"
    global fixture

    # check if fixture does not exist
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
    else:
        # check if the existing fixture is corrupted
        if not fixture.is_valid():
            # create a new fixture and perform login
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
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

