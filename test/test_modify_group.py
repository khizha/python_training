# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="asd_upd", header="asd_upd", footer="asd_upd"))
    app.session.logout()

