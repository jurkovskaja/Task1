# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application_contact

# init fixture
@pytest.fixture
def app(request):
    fixture = Application_contact()
    # an indication of how fixture should be destroyed
    request.addfinalizer(fixture.destroy)
    return fixture

def test_Task2_add_contact(app):
   app.login(username="admin", password="secret")
   app.create_contact(Contact(firstname="qwee", middlename="qwere", lastname="qwerqwetqe", nickname="dfgfdg",
                            title="dfgnhgf", company="sdfsdfsdf", address="qwerwreqer", home="11", mobile_phone="22",
                            work_phone="33", fax="444", email="5555", email2="666", email3="777", homepage="sadffasd",
                            address2="1wrtrewer", phone2="phone2", notes="sdfgnvbxfgsdf", date="option[18]",
                            month="option[12]", byear="123", aday="option[31]", amonth="option[2]", ayear="1231"))
   app.logout()

