from model.group import Group


def test_change_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.change_first_group()

