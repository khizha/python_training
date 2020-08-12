# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    # if groups list is empty
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    old_groups = app.group.get_group_list()

    # select random group for deletion
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)

    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    # remove first element from the old list of groups
    old_groups[index:index+1] =[]
    assert old_groups == new_groups