# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="qwee", middlename="qwere", lastname="qwerqwetqe", nickname="dfgfdg",
                                   title="dfgnhgf", company="sdfsdfsdf", address="qwerwreqer", home="11",
                                   mobile_phone="22",
                                   work_phone="33", fax="444", email="5555", email2="666", email3="777",
                                   homepage="sadffasd",
                                   address2="1wrtrewer", phone2="phone2", notes="sdfgnvbxfgsdf", date="option[18]",
                                   month="option[12]", byear="123", aday="option[31]", amonth="option[2]",
                                   ayear="1231"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

