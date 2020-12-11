# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

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
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()

    app.contact.open_new_contact_page()
    app.contact.fill_in_new_contact_data(contact)
    app.contact.submit_created_contact()

     # check that the new contacts list is 1 element longer than the old list
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()

    max_ = new_contacts[0].id
    for i in new_contacts:
        if i.id > max_:
            max_ = i.id

    contact.id = max_
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
