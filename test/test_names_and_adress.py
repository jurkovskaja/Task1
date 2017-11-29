from model.contact import Contact

def test_names_and_address_on_home_page(app, db):
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_list()
    # получаем информацию из БД
    contact_from_db = db.get_contact_list()
    # сравниваем между собой
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)