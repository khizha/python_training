# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string_for_names(prefix, maxlen):
    # random string generating method

    # only letters
    symbols = string.ascii_letters

    # generate a random string with random length, but not longer than maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_address(prefix, maxlen):
    # random string generating method

    # letters, new lines, punctuation symbols, digits, whitespaces
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10 + "/n"*4

    # generate a random string with random length, but not longer than maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_email(prefix, maxlen):
    # letters, digits
    symbols = string.ascii_letters + string.digits

    # generate a random string with random length, but not longer than maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(symbols) for i in range(random.randrange(3))])

def random_string_for_phone(prefix, maxlen):
        # random string generating method

        # digits
        symbols = string.digits

        # generate a random string with random length, but not longer than maxlen
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", phone2="", email="", email2="", email3="")] + [
    Contact(firstname=random_string_for_names("firstname", 7),
            lastname=random_string_for_names("lastname", 10),
            address=random_string_for_address("address", 40),
            homephone=random_string_for_phone("homephone", 8),
            mobilephone=random_string_for_phone("mobilephone", 8),
            workphone=random_string_for_phone("workphone", 8),
            phone2=random_string_for_phone("phone2", 8),
            email=random_string_for_email("email", 10),
            email2=random_string_for_email("email2", 10),
            email3=random_string_for_email("email3", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))