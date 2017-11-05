# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="contact")
    cont.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_contact_firstname(cont)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


