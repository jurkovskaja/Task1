import re


def test_phones_on_home_page(app):
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    # получаем информацию со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # сравниваем между собой
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)


def test_phones_on_contact_view_page(app):
    # получаем информацию со страницы просмотра
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    # получаем информацию со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # сравниваем между собой
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


# функция для замены символов, которые нам "мешают"/не отображаются на гл.страницу
def clear(s):
    return re.sub("[() -]", "", s)
