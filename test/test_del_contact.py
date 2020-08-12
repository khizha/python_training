# -*- coding: utf-8 -*-
import time

def test_delete_first_contact(app):
    # if contacts list is empty
    if app.contact.count() != 0:
        old_contacts = app.contact.get_contacts_list()
        app.contact.delete_first_contact()
        time.sleep(3)
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contacts_list()
        # remove first element from the old list of contacts
        old_contacts[0:1] = []
        assert old_contacts == new_contacts