# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact_firstname(Contact(firstname="contact"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


