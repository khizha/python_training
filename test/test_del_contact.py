# -*- coding: utf-8 -*-
import random
from model.contact import Contact

def test_delete_first_contact(app, db, check_ui):
    # if contacts list is empty
    if app.contact.count() != 0:
        old_contacts = db.get_contact_list()

        # get a random contact from the contacts list
        target_contact = random.choice(old_contacts)

        # delete the selected contact by id
        app.contact.delete_contact_by_id(target_contact.id)

        #time.sleep(3)
        assert len(old_contacts) - 1 == app.contact.count()

        new_contacts = db.get_contact_list()

        # remove contacts list element that is equal to the given parameter
        old_contacts.remove(target_contact)
        assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)