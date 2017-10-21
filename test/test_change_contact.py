def test_change_first_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.change_first_contact()
    app.session.logout()