from random import randrange


def test_names_and_address_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[index]
    # получаем информацию со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
   # сравниваем между собой
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

