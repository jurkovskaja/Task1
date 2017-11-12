from random import randrange


def test_email_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    # получаем информацию с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[index]
    # получаем информацию со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # сравниваем содержимое ячейки'All email' c результатом склейки
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


# функция склеивающая все email
def merge_email_like_on_home_page(contact):
    return "\n".join((filter(lambda x: x != "", # выкидываем пустые строки
                             filter(lambda x: x is not None, # выкидываем строки имеющие значени "None"
                                    [contact.email, contact.email2, contact.email3]))))
