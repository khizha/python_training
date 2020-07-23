# -*- coding: utf-8 -*-
from model.group import Group

#def test_modify_group(app):
#    app.session.login(username="admin", password="secret")
#    app.group.modify(Group(name="asd_upd", header="asd_upd", footer="asd_upd"))
#    app.session.logout()

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New Group"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
