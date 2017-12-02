import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app, db):
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_phones_list()
    # получаем информацию из БД
    contact_from_db = db.get_contacts_email_list()
    for contact in contact_from_db:
        contact.all_phones_from_home_page = merge_phones_like_on_home_page(contact)
    # сравниваем
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


def test_phones_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    # получаем информацию со страницы просмотра
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    # получаем информацию со страницы редактирования
    app.contact.click_on_home_link()
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # сравниваем между собой
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


# функция для замены символов, которые нам "мешают"/не отображаются на гл.странице
def clear(s):
    return re.sub("[() -]", "", s)

# функция склеивающая все номера телефонов
def merge_phones_like_on_home_page(contact):
    return "\n".join((filter(lambda x: x != "", # выкидываем пустые строки
                              map(lambda x: clear(x), # выкидываем лишние символы
                                  filter(lambda x: x is not None,# выкидываем строки имеющие значени "None"
                                         [contact.home,contact.mobile_phone,contact.work_phone, contact.phone2])))))

