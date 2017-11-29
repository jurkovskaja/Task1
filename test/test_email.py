from model.contact import Contact
from random import randrange

def test_email_on_home_page(app,db):
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    # получаем информацию со страницы редактирования
    contact_from_db_page = db.get_contacts_email_list()
    # сравниваем содержимое ячейки'All email' c результатом склейки
    assert (contact_from_home_page.all_email_from_home_page).split('\n') == merge_email_like_on_home_page(contact_from_db_page)


# функция склеивающая все email
def merge_email_like_on_home_page(contact):
    return "\n".join((filter(lambda x: x != "", # выкидываем пустые строки
                             filter(lambda x: x is not None, # выкидываем строки имеющие значени "None"
                                   [contact.email, contact.email2, contact.email3]))))

