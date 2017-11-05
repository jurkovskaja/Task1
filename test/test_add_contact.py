# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    cont = Contact(firstname="5558", middlename="qwere", lastname="qwerqwetqe", nickname="dfgfdg",
                              title="dfgnhgf", company="sdfsdfsdf", address="qwerwreqer", home="11", mobile_phone="22",
                              work_phone="33", fax="444", email="5555", email2="666", email3="777", homepage="sadffasd",
                              address2="1wrtrewer", phone2="phone2", notes="sdfgnvbxfgsdf", date="option[18]",
                              month="option[12]", byear="123", aday="option[31]", amonth="option[2]", ayear="1231")
    app.contact.create(cont)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


