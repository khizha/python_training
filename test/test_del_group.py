# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    # if groups list is empty
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()

    # select random group for deletion
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)

    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    # remove group element that is equal to the given parameter
    old_groups.remove(group)
    assert old_groups == new_groups
    # switchable verification of the new list of groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)