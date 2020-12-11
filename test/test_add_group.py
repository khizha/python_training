# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    # random string generating method

    # all the symbols, punctuation symbols and 10 whitespaces
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10

    # generate a random string with random length, but not longer than maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# test data will contain random names with prefix "name" and length not more than 10; footer with prefix "footer" and length<=20; same for header
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#    for footer in ["", random_string("footer", 20)]
#]
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
        old_groups=app.group.get_group_list()
        app.group.create(group)
        # check that the new groups list is 1 element longer than the old lis
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        #app.session.logout()


