# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


# init fixture
@pytest.fixture
def app(request):
    fixture = Application()
    # an indication of how fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture

def test_Task2_add_group(app):
    app.session.login(username="admin",password="secret")
    app.create_group(Group(name="Task2", header="Task2", footer="Task2"))
    app.session.logout()

def test_Task2_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

