# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

# init fixture
@pytest.fixture
def app(request):
    fixture = Application()
    # an indication of how fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture

def test_Task2_add_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name="Task2", header="Task2", footer="Task2"))
    app.logout()

def test_Task2_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

