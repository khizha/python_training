# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

constant =[
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def random_string(prefix, maxlen):
    # random string generating method

    # all the symbols, punctuation symbols and 10 whitespaces
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10

    # generate a random string with random length, but not longer than maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# test data will contain random names with prefix "name" and length not more than 10; footer with prefix "footer" and length<=20; same for header

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]
