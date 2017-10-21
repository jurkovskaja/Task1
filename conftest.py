import pytest
from fixture.application import Application

# init fixture
@pytest.fixture (scope="session")
def app(request):
    fixture = Application()
    # an indication of how fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture