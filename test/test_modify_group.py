# -*- coding: utf-8 -*-
from model.group import Group

#def test_modify_group(app):
#    app.session.login(username="admin", password="secret")
#    app.group.modify(Group(name="asd_upd", header="asd_upd", footer="asd_upd"))
#    app.session.logout()

def test_modify_group_name(app):
    if app.group.count() != 0:
        old_groups = app.group.get_group_list()
        group=Group(name="New Group")
        group.id = old_groups[0].id
        app.group.modify_first_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() != 0:
#        old_groups = app.group.get_group_list()
#        app.group.modify_first_group(Group(header="New header"))
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)
