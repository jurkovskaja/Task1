# -*- coding: utf-8 -*-
from model.group import Group

def test_Task2_add_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="Task2", header="Task2", footer="Task2"))
    app.session.logout()

def test_Task2_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

