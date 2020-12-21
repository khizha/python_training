# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

#def test_modify_group(app):
#    app.session.login(username="admin", password="secret")
#    app.group.modify(Group(name="asd_upd", header="asd_upd", footer="asd_upd"))
#    app.session.logout()

def test_modify_group_name(app, db, check_ui):
    #if db.group.count() != 0:
    if len(db.get_group_list()) != 0:
        old_groups = db.get_group_list()
        index = randrange(len(old_groups))

        group = Group(name="New Group")
        group.id = old_groups[index].id

        group.header = old_groups[index].header
        group.footer = old_groups[index].footer

        #app.group.modify_group_by_index(index, group)
        app.group.modify_group_by_id(group.id, group)
        assert len(old_groups) == len(db.get_group_list())
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count() != 0:
#        old_groups = app.group.get_group_list()
#        app.group.modify_first_group(Group(header="New header"))
#        new_groups = app.group.get_group_list()
#        assert len(old_groups) == len(new_groups)
