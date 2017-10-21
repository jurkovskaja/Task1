def test_Task2_delete_first_group(app):
    app.session.login(username="admin",password="secret")
    app.group.delete_first_group()
    app.session.logout()