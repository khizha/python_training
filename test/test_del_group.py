# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    # if groups list is empty
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # remove first element from the old list of groups
    old_groups[0:1] =[]
    assert old_groups == new_groups