# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


# генерация случайных строк не превышаюших длину maxlen
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=(random_string("adress", 10)),
            home=random_string("home", 10), mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            phone2=random_string("phone", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), middlename="", nickname="", title="", company="", fax="", homepage="",
            address2="", notes="", date="", byear="", ayear="")
            for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])


def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


