# -*- coding: utf-8 -*-
from model.contact import Contact


def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="qwee", middlename="qwere", lastname="qwerqwetqe", nickname="dfgfdg",
                                   title="dfgnhgf", company="sdfsdfsdf", address="qwerwreqer", home="11",
                                   mobile_phone="22",
                                   work_phone="33", fax="444", email="5555", email2="666", email3="777",
                                   homepage="sadffasd",
                                   address2="1wrtrewer", phone2="phone2", notes="sdfgnvbxfgsdf", date="option[18]",
                                   month="option[12]", byear="123", aday="option[31]", amonth="option[2]",
                                   ayear="1231"))
    app.contact.change_first_contact()
