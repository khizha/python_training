# -*- coding: utf-8 -*-
from model.group import Group

# load test data from groups.json file which resides in data package (see data_groups argument)
def test_add_group(app, json_groups):
        group = json_groups
        old_groups=app.group.get_group_list()
        app.group.create(group)
        # check that the new groups list is 1 element longer than the old lis
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        #app.session.logout()


