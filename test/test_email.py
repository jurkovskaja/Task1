from model.contact import Contact
from random import randrange

def test_email_on_home_page(app,db):
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_email_list()
    # получаем информацию из БД
    contact_from_db = db.get_contacts_email_list()
    for contact in contact_from_db:
        contact.all_email_from_home_page = merge_email_like_on_home_page(contact)
    # сравниваем
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


# функция склеивающая все email
def merge_email_like_on_home_page(contact):
    return "\n".join((filter(lambda x: x != "", # выкидываем пустые строки
                             filter(lambda x: x is not None, # выкидываем строки имеющие значени "None"
                                   [contact.email, contact.email2, contact.email3]))))

